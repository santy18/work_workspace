## 1. Password Hygiene Auditor (Offline)
- **What**: Reviews exported vault data to flag weak/duplicate passwords.
- **How it works**:
  - Parses local CSV/JSON export.
  - Produces a prioritized fix list.
- **Why now**: Enhances security without exposing user passwords.

## 2. Internal Phishing Simulator & Coach (Security)
- **What**: Generates realistic internal phishing tests and teaches safe responses.
- **How it works**:
  - Crafts scenario emails and landing pages.
  - Scores responses and provides instant feedback.
- **Why now**: Utilizes open weights for effective training.

## 3. First-Party Creative Studio (Marketing)
- **What**: Generates tailored ad content without sending data externally.
- **How it works**:
  - Reads CRM/exported analytics to build segment personas.
  - Creates ad headlines, body copy, and visuals.

## 4. Compliance Checklist Builder (Legal)
- **What**: Generates to-do lists for new compliance requirements (e.g., GDPR).
- **How it works**:
  - Analyzes policies and new rule texts.
  - Outputs tasks, owners, and deadlines.

## 5. Access Log Anomaly Summarizer (Security)
- **What**: Highlights unusual logins in simple language.
- **How it works**:
  - Parses SIEM exports locally.
  - Produces daily digests with prioritized follow-ups.

## 6. Invoice Reconciliation Agent (Finance)
- **What**: Matches invoices to purchase orders and flags mismatches.
- **How it works**:
  - Parses PDFs/CSVs.
  - Outputs a reconciliation report.

## 7. Internal Code Secret & Vulnerability Scanner (Security)
- **What**: Finds leaked tokens and vulnerabilities in code.
- **How it works**:
  - Scans Git diffs, repositories, and config files on-prem.
  - Outputs a rotation checklist and commit suggestions.

## 8. On-Prem Patient Intake Summarizer (Healthcare)
- **What**: Converts messy patient notes into structured summaries.
- **How it works**:
  - Parses PDFs/portal messages.
  - Extracts relevant medical information.

## 9. Private Code Review Copilot (Dev)
- **What**: Reviews code diffs and suggests fixes without leaving the repository.
- **How it works**:
  - Runs in your VPC/CI runner.
  - Outputs comments and patches.

## 10. Internal Knowledgebase Chat (Org-wide)
- **What**: Answers organizational queries using internal resources.
- **How it works**:
  - Local retrieval over network shares/wikis.
  - Returns answers with source links.

## 11. License & Policy Aware Code Assistant (Dev)
- **What**: Suggests compliant code patterns based on internal policies.
- **How it works**:
  - Ingests policy repositories and license allowlists.
  - Suggests compliant code snippets.

## 12. Account-Based Personalizer (ABM, On-Prem)
- **What**: Creates personalized emails and landing pages.
- **How it works**:
  - Ingests target personas and usage data.
  - Generates tailored value propositions.

## 13. Internal API Chat Gateway (Dev)
- **What**: Facilitates task execution via internal services.
- **How it works**:
  - Implements strict schemas for service actions.
  - Requires human approvals.

## 14. On-Prem Support Ticket Summarizer (IT/Support)
- **What**: Summarizes support tickets and suggests actions.
- **How it works**:
  - Reads helpdesk exports locally.
  - Provides structured triage and draft replies.

## 15. Personal Finance Vault (Consumer Finance)
- **What**: Offers private budgeting and cash flow insights.
- **How it works**:
  - Ingests bank CSV exports.
  - Produces budgets and change briefs.

## 16. GDPR-Friendly Customer Inbox Triage (EU Orgs)
- **What**: Classifies customer emails with minimal data movement.
- **How it works**:
  - Processes data locally; only metadata may leave.
  - Implements role-aware routing.

## 17. Contract Clause Finder (Legal)
- **What**: Locates specific clauses in contracts.
- **How it works**:
  - Indexes clauses locally.
  - Provides jump-to-section answers.

## 18. Clinician Note De-Jargonizer (Personal Healthcare)
- **What**: Converts clinical notes into patient-friendly language.
- **How it works**:
  - On-device app ingests medical summaries.
  - Outputs readable instructions.

## 19. Private Meeting Minutes & Action Extractor (Org)
- **What**: Transforms meetings into decisions and tasks.
- **How it works**:
  - Summarizes audio/text locally.
  - Exports actions to project management tools.