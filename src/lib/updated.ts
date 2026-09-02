// Returns the previous calendar month as "Month Year" (e.g. build in Sep 2026 -> "August 2026").
// This runs at BUILD time (Astro is statically rendered), so the displayed date only
// changes on the next deploy, not on every page visit. See .github/workflows/monthly-rebuild.yml
// for the automation that redeploys on the 1st of each month so this stays current without
// manual edits.
export function getLastUpdated(): string {
  const now = new Date();
  const prevMonth = new Date(now.getFullYear(), now.getMonth() - 1, 1);
  return prevMonth.toLocaleDateString('en-US', { month: 'long', year: 'numeric' });
}
