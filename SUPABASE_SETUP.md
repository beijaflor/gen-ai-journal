# Supabase Setup Guide

## Phase 1: Create Supabase Project

### Step 1: Create Account and Project

1. Go to [supabase.com](https://supabase.com)
2. Sign up or log in
3. Click "New Project"
4. Fill in project details:
   - **Project name**: gen-ai-journal (or your choice)
   - **Database password**: (generate and save securely)
   - **Region**: Choose closest to you (e.g., Tokyo for Japan)
   - **Pricing plan**: Free tier is sufficient
5. Wait for project provisioning (~2 minutes)

### Step 2: Get API Credentials

1. Go to **Project Settings** (gear icon in sidebar)
2. Click **API** in the left menu
3. Copy and save these values:
   - **Project URL** (e.g., `https://xxx.supabase.co`)
   - **anon public key** (starts with `eyJ...`)
   - **service_role key** (starts with `eyJ...`, keep secret!)

### Step 3: Create Database Schema

1. Go to **SQL Editor** in the left sidebar
2. Click **New query**
3. Paste and run the following SQL:

```sql
-- Create summary_metadata table
CREATE TABLE summary_metadata (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  summary_id VARCHAR(10) NOT NULL,      -- e.g., "001"
  url TEXT NOT NULL,                     -- Source URL
  journal_date DATE,                     -- NULL = workdesk, set = published

  -- Flags
  annex_flag BOOLEAN DEFAULT FALSE,      -- Mark for annex journal
  standout_flag BOOLEAN DEFAULT FALSE,   -- Exceptional content
  omit_flag BOOLEAN DEFAULT FALSE,       -- Exclude from both journals
  upvote_flag BOOLEAN DEFAULT FALSE,     -- Curator upvote
  downvote_flag BOOLEAN DEFAULT FALSE,   -- Curator downvote

  -- Scores
  ai_scores JSONB,                       -- Preserved AI scores

  -- Audit
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  updated_by UUID REFERENCES auth.users(id),

  UNIQUE(summary_id, url),
  CHECK (NOT (annex_flag AND omit_flag))
);

-- Create indexes for fast lookups
CREATE INDEX idx_summary_metadata_id ON summary_metadata(summary_id);
CREATE INDEX idx_summary_metadata_url ON summary_metadata(url);
CREATE INDEX idx_summary_metadata_date ON summary_metadata(journal_date);
CREATE INDEX idx_summary_metadata_flags ON summary_metadata(annex_flag, standout_flag, omit_flag, upvote_flag, downvote_flag);

-- Enable Row Level Security
ALTER TABLE summary_metadata ENABLE ROW LEVEL SECURITY;

-- Policy: Anyone can read published summaries
CREATE POLICY "Public read access" ON summary_metadata
  FOR SELECT USING (journal_date IS NOT NULL);

-- Policy: Authenticated users can read workdesk summaries
CREATE POLICY "Authenticated read workdesk" ON summary_metadata
  FOR SELECT USING (auth.role() = 'authenticated');

-- Policy: Authenticated users can insert/update
CREATE POLICY "Authenticated write" ON summary_metadata
  FOR ALL USING (auth.role() = 'authenticated');
```

4. Click **Run** to execute the schema

### Step 4: Enable Authentication

1. Go to **Authentication** in the left sidebar
2. Click **Providers**
3. Ensure **Email** is enabled (should be enabled by default)
4. Optionally configure email templates under **Email Templates**

### Step 5: Create Admin User

1. Go to **Authentication** → **Users**
2. Click **Add user** → **Create new user**
3. Fill in:
   - **Email**: Your admin email
   - **Password**: Choose a secure password
   - **Auto Confirm User**: Toggle ON (skip email confirmation)
4. Click **Create user**

### Step 6: Configure Environment Variables

Now you have everything needed for the next phase. Save these values:

```
PROJECT_URL=https://xxx.supabase.co
ANON_KEY=eyJhbGc...
SERVICE_ROLE_KEY=eyJhbGc... (keep secret!)
ADMIN_EMAIL=your-email@example.com
ADMIN_PASSWORD=your-password
```

## Next Steps

Phase 1 is complete! You can now proceed to Phase 2 where we'll integrate Supabase into your Astro application.

The following files will be created:
- `website/src/lib/supabase.ts` - Client library
- `website/src/lib/supabase-cache.ts` - Build-time caching
- `website/src/pages/auth/login.astro` - Login page
- And more...
