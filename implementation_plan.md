# Implementation Plan

[Overview]
This plan outlines the steps to remove the GitHub Pages deployment functionality from the project's CI/CD pipeline. This involves deleting the deployment script, removing the deployment job from the GitHub Actions workflow, and updating the Makefile.

[Types]
There are no changes to types, data structures, or interfaces.

[Files]
File modifications will be made to remove the GitHub Pages deployment logic.

- **Modified:** `.github/workflows/ci.yml` - The `deploy` job will be removed.
- **Deleted:** `scripts/build_readme_pages.py` - This script is no longer needed.
- **Modified:** `Makefile` - The `ci` target will be updated to remove any deployment-related steps.

[Functions]
No new, modified, or removed functions.

[Classes]
No new, modified, or removed classes.

[Dependencies]
No changes to dependencies.

[Testing]
No changes to the testing approach.

[Implementation Order]
1. Modify `.github/workflows/ci.yml` to remove the `deploy` job.
2. Delete the `scripts/build_readme_pages.py` file.
3. Modify the `Makefile` to update the `ci` target.
