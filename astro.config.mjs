// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// IMPORTANT: update `site` to the real domain once the purchase is confirmed.
export default defineConfig({
  site: 'https://kseniiashermin.com',
  integrations: [sitemap()],
});
