import { createClient } from '@supabase/supabase-js';

// Types for our database tables
export interface SummaryMetadata {
  id: string;
  summary_id: string;
  url: string;
  journal_date: string | null;
  annex_flag: boolean;
  standout_flag: boolean;
  omit_flag: boolean;
  upvote_flag: boolean;
  downvote_flag: boolean;
  ai_scores: AiScores | null;
  created_at: string;
  updated_at: string;
  updated_by: string | null;
}

export interface AiScores {
  signal?: number;
  depth?: number;
  unique?: number;
  practical?: number;
  antiHype?: number;
  mainJournal?: number;
  annexPotential?: number;
  overall?: number;
}

export interface Database {
  public: {
    Tables: {
      summary_metadata: {
        Row: SummaryMetadata;
        Insert: Omit<SummaryMetadata, 'id' | 'created_at' | 'updated_at'>;
        Update: Partial<Omit<SummaryMetadata, 'id' | 'created_at'>>;
      };
    };
  };
}

// Get environment variables
const supabaseUrl = import.meta.env.PUBLIC_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.PUBLIC_SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseAnonKey) {
  console.warn(
    'Supabase environment variables not found. Admin features will be disabled.'
  );
}

// Create Supabase client
export const supabase = createClient<Database>(
  supabaseUrl || '',
  supabaseAnonKey || '',
  {
    auth: {
      persistSession: true,
      autoRefreshToken: true,
    },
  }
);

// Helper to check if user is authenticated
export async function isAuthenticated(): Promise<boolean> {
  const {
    data: { user },
  } = await supabase.auth.getUser();
  return !!user;
}

// Helper to get current user
export async function getCurrentUser() {
  const {
    data: { user },
  } = await supabase.auth.getUser();
  return user;
}

// Helper to sign in
export async function signIn(email: string, password: string) {
  return await supabase.auth.signInWithPassword({ email, password });
}

// Helper to sign out
export async function signOut() {
  return await supabase.auth.signOut();
}

// Helper to get summary metadata
export async function getSummaryMetadata(
  summaryId: string,
  url: string
): Promise<SummaryMetadata | null> {
  const { data, error } = await supabase
    .from('summary_metadata')
    .select('*')
    .eq('summary_id', summaryId)
    .eq('url', url)
    .single();

  if (error) {
    if (error.code === 'PGRST116') {
      // No rows found
      return null;
    }
    console.error('Error fetching summary metadata:', error);
    return null;
  }

  return data;
}

// Helper to upsert summary metadata
export async function upsertSummaryMetadata(
  metadata: Partial<SummaryMetadata> & {
    summary_id: string;
    url: string;
  }
): Promise<SummaryMetadata | null> {
  const user = await getCurrentUser();

  const { data, error } = await supabase
    .from('summary_metadata')
    .upsert(
      {
        ...metadata,
        updated_at: new Date().toISOString(),
        updated_by: user?.id || null,
      },
      {
        onConflict: 'summary_id,url',
      }
    )
    .select()
    .single();

  if (error) {
    console.error('Error upserting summary metadata:', error);
    return null;
  }

  return data;
}

// Helper to get all workdesk summaries metadata
export async function getWorkdeskMetadata(): Promise<SummaryMetadata[]> {
  const { data, error } = await supabase
    .from('summary_metadata')
    .select('*')
    .is('journal_date', null);

  if (error) {
    console.error('Error fetching workdesk metadata:', error);
    return [];
  }

  return data || [];
}

// Helper to get metadata for a specific journal
export async function getJournalMetadata(
  journalDate: string
): Promise<SummaryMetadata[]> {
  const { data, error } = await supabase
    .from('summary_metadata')
    .select('*')
    .eq('journal_date', journalDate);

  if (error) {
    console.error('Error fetching journal metadata:', error);
    return [];
  }

  return data || [];
}
