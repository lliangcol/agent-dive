# SecurityPolicy

AgentDive mainly includes AI Agent project learning materials, templates, diagrams and lightweight verification scripts. Even if it is not currently a runtime service, public repositories still need to avoid leaking keys, private paths, and unauthorized third-party content.

## Support range

Security reports apply to:

- Keys, tokens, accounts, private paths or internal configurations mistakenly submitted in the repository.
- Issues in verification scripts, templates or document processes that may induce users to disclose sensitive information.
- Problems with license violations, incorrect attribution, or unauthorized content in third-party project collection materials.
- Permissions and supply chain risks in GitHub Actions, Issue/PR templates, or automation configurations.

not applicable to:

- The vulnerabilities of the third-party project itself are collected. Please give priority to reporting to the corresponding upstream project.
- Generic AI Agent safety discussion without impact paths.
- Abstract risks that cannot be pinned down to specific files, processes, or contribution paths.

## Reporting method

If your GitHub repository has private vulnerability reporting enabled, please use this entry first. Otherwise, please create an Issue that does not disclose sensitive details, stating that you need to report the security issue privately, or contact the security contact listed in the maintainer's public profile.

Please include in your report:

- Affected files, directories, templates or processes.
- Steps to reproduce or specific evidence.
- Potential scope of impact.
- Suggest directions for repair.

Do not paste real keys, tokens, account numbers, private URLs, internal paths, or complete exploit details that could be abused in public issues.

## Maintainer response

The maintainer will first confirm whether the report affects the repository, and if necessary, remove relevant content, revoke exposed credentials, correct documents, or adjust automation permissions. Once the fix is ​​complete, the scope of the impact and how it was verified should be documented in a PR or release notes, but sensitive material should not be made public.