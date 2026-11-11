# Diagram & publication standards

## Mermaid
Use readable stable node IDs; differentiate normative edges (solid) from illustrative/conditional transitions (dashed). Always explain this legend in the Markdown report.

## SVG
SVG is genuine UTF-8 vector XML with `<title>` and `<desc>`. The generator shows paths in distinct lanes with accessible node text and a disclaimer. Keep labels legible; do not substitute PNG screenshots for vector assets or hotlink arbitrary third-party diagrams.

## Markdown report
One main H1, jurisdiction/date at top, relative `./route.svg` embedded near the top, alternative pathways, detailed role explanations, eligibility requirements, negative constraints/uncertainty and verified external sources. Avoid absolute GitHub image URLs, so Pages and repository Markdown both resolve.

## Website
Static generator discovers `data/*/*/route.json`; index, category search, route detail, SVG, Mermaid, sitemap and catalog JSON must be built from that data, not manually maintained lists. Keep site working under GitHub Pages project subpath `/job-route/`.

## Deployment
CI: validate JSON/schema/source references, check diagram drift, run tests, build static site, smoke-test outputs. For `main`, deploy using official `configure-pages@v5`, `upload-pages-artifact@v4`, `deploy-pages@v4`. Repository Settings → Pages → Source: **GitHub Actions** must be enabled to deploy. Do not state that site was published until actual workflow and live URL confirm it.
