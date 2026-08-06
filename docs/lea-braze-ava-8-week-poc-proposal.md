# Ava: 8-Week Request-to-Quote POC

**Prepared for:** Jim and Lea & Braze

**Date:** August 6, 2026

**Decision requested:** Approve a controlled eight-week engagement to determine whether Ava can prepare routine project quote packages faster, with acceptable accuracy, while Lea & Braze retains final authority.

## Purpose and POC Boundary

Ava will work beside the existing quote process, not replace it. She will receive copies of approved inquiries, organize the request, identify missing information, research the property and jurisdiction, retrieve approved comparable quotes, prepare a branded draft package, and present it for review. Jim or another named Lea & Braze reviewer retains professional judgment, pricing authority, and approval of the exact customer message and attachment.

The measured POC is limited to one common quote family, up to three jurisdictions, one to three approved layouts, at least 50 reviewed historical cases, and a target of 15-25 eligible parallel cases. The existing workflow and Monday.com remain unchanged.

**Included:** Exchange Online intake, approved attachments, ArcGIS/public research, a controlled SMB/DFS data subset, comparable-quote retrieval, quote drafting, Teams notifications, an authenticated review dashboard, audit history, and an approval-gated final send.

**Excluded:** company-wide rollout, all 16-17 TB of company data, unrestricted file access, autonomous pricing commitments, engineering/code conclusions, full plan interpretation, Monday.com replacement, SWPPP, and unsupervised customer communication.

## Recommended Deployment and Integration

```text
Exchange Online mailbox -> Microsoft Graph -> Ava workflow in AWS
  -> approved SMB/DFS subset over existing Site-to-Site VPN
  -> ArcGIS/public sources + approved model API
  -> Teams notification + Entra-authenticated review dashboard
  -> named human approval -> Microsoft Graph sends the exact approved package
```

| Area | POC decision |
| --- | --- |
| **Hosting** | Run the Python service on a small, hardened AWS instance in a private subnet because Lea & Braze already has AWS and a Site-to-Site connection. Use managed PostgreSQL for workflow/audit state, encrypted object storage for POC artifacts, Secrets Manager, and CloudWatch logs/alerts. No public SMB, database, or admin endpoint. |
| **Email and identity** | IT creates a company-controlled Ava POC mailbox and adds it to the approved `info`/`RFP` distribution lists. A dedicated Entra application uses Microsoft Graph with only required mail permissions. Exchange Online RBAC scopes application access to Ava's mailbox. `Mail.Send` is enabled only for the controlled-send stage. |
| **Teams and approval** | A private POC channel receives status and review notifications. Approval occurs in the Entra-authenticated dashboard reached from the Teams card, providing an unambiguous approver, artifact version, timestamp, and audit record. Natural-language Teams replies do not directly authorize a send. |
| **Files** | IT provides one read-only POC input folder and a separate output folder. Ava reaches them through the existing AWS private connection using a dedicated on-premises service identity. Only approved templates and historical cases are indexed; source files cannot be modified. |
| **Data controls** | Use only the approved POC subset and minimum necessary content. Region, retention, deletion, model-provider use, malware scanning, backup, and incident contacts are documented before live cases. Every file read, model call, draft, edit, approval, and send is logged. |

<div style="page-break-after: always;"></div>

## Agent Harness and Models

The **existing Python workflow controller remains Ava's harness**. It already implements Graph intake, deterministic workflow gates, ArcGIS research, quote generation, human review, duplicate suppression, and structured model output. For the POC it will move from local JSON state to PostgreSQL and add production retries, idempotency, audit events, and health alerts.

Ava is one user-facing digital worker with bounded internal capabilities: intake, completeness checking, research, comparable retrieval, quote assembly, and quality control. Models may interpret and draft, but they cannot change permissions, browse arbitrary company files, approve work, or send email. Deterministic Python code owns every state change and external action.

**Model plan:** use OpenAI's Responses API with strict JSON schemas. Establish the quality baseline with **GPT-5.6 Terra** for extraction, research synthesis, comparable analysis, and drafting. After evaluation, move only proven low-risk classification and field extraction to **GPT-5.6 Luna** for lower cost and latency. Use `text-embedding-3-large` for comparable-quote retrieval. Pin model/prompt versions during measured testing and rerun the golden test set after any change. If those models are unavailable in the approved account, use the current IT-approved equivalents and record the exact versions.

**Harness decision:** do not migrate the POC to Hermes. Hermes is a broad, self-improving personal-agent platform with persistent memory and terminal/browser tools; those capabilities add migration effort and control surface without improving this fixed, auditable quote workflow. OpenClaw may remain available for the existing demo, but it will not own POC state or business actions. The production POC calls the model API and Microsoft interfaces through narrowly scoped adapters in the Python service.

## Eight-Week Delivery Plan

| Weeks | Work and exit result |
| --- | --- |
| **1-2: Define and connect** | Confirm quote family, reviewers, baseline, approved historical set, data rules, and stop/escalation policy. Deploy the AWS environment; configure Entra/Graph, Ava mailbox, Teams channel, dashboard sign-in, secrets, logging, and private network access. **Exit:** IT-approved nonproduction path with outbound sending disabled. |
| **3-4: Build the controlled workflow** | Connect the approved SMB folders, migrate durable state, index approved comparables, validate ArcGIS research, configure model schemas/prompts, and reproduce Lea & Braze's quote format. **Exit:** historical inquiry produces a source-linked draft package. |
| **5-6: Evaluate and harden** | Add dashboard approval, audit history, alerts, retries, duplicate prevention, attachment checks, backup/restore, and emergency shutoff. Replay the golden historical set and correct systematic failures. **Exit:** safety tests pass and quality reaches the parallel-run threshold. |
| **7-8: Parallel run and decision** | Run Ava beside the existing process on eligible inquiries. Measure speed, hands-on time, corrections, and operating cost. Customer sending remains disabled unless Jim and IT authorize a monitored controlled-send window. **Exit:** scorecard, risk register, operating runbook, and go/revise/stop recommendation. |

## Pass/Fail Measures

The POC proceeds beyond parallel testing only when safety and business value pass together:

- **0** unauthorized, duplicate, wrong-recipient, or wrong-attachment sends.
- At least **80%** of routine first-pass Ava packages have no material error or omission and perform no worse than the manual first pass.
- Median time and human hands-on effort to a materially acceptable package are at least **50% lower** than the manual baseline.
- Median reviewer hands-on time for a routine complete package is **10 minutes or less**.
- **100%** of measured cases preserve sources, model/prompt version, output versions, human changes, approval identity, and final action.
- Uncertain jurisdiction, missing information, unsupported pricing, or out-of-scope work reliably stops for human review.

## Deliverables and Responsibilities

**POC deliverables:** working AWS-hosted Ava workflow; configured mailbox, Teams, dashboard, file connector, research and quote pipeline; historical and parallel-run test results; security and operations runbook; case-level audit export; final scorecard; and a scoped MVP recommendation.

**Lea & Braze provides:** Jim's business decisions and final approvals; IT-created identities, permissions, network rules, POC folders, and incident contacts; timely access to at least 50 approved historical cases and selected templates; two to four pilot reviewers; and confirmation of permitted data/model use.

**Consultant provides:** implementation, migration of the demonstrated workflow, configuration support, testing, monitoring during the POC, documentation, weekly status, and the final recommendation. Lea & Braze owns all professional and commercial decisions.

## Approval

Approval authorizes the bounded POC and not a production rollout or autonomous customer communication.

| Lea & Braze approval | Date |
| --- | --- |
|  |  |
