// Kick the summarization DO (#166). Shared by link submission and retry.
import type { Env } from "./auth";

export function enqueueSummarization(env: Env): Promise<unknown> | null {
  if (env.AUTO_SUMMARIZE !== "true" || !env.SUMMARIZER) return null;
  const stub = env.SUMMARIZER.get(env.SUMMARIZER.idFromName("main"));
  return stub.fetch("https://summarizer/enqueue", { method: "POST" }).catch(() => {});
}
