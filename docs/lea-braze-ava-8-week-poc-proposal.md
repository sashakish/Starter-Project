# Ava: 8-Week Agentic Request-to-Quote POC

**Prepared for:** Jim and Lea & Braze

**Date:** August 6, 2026

**Decision requested:** Approve a controlled eight-week engagement to determine whether an LLM-backed Ava can prepare project quote packages faster, answer quote-related questions in Teams, and learn from approved corrections while Lea & Braze retains final authority.

## Purpose and POC Boundary

During the measured POC, Ava works beside the existing quote process so her results can be compared safely. This is a validation posture, not the permanent design: if the gates pass, a later phase can progressively make Ava the primary quote-preparation workflow. Jim or another named reviewer retains professional judgment, pricing authority, and approval of the exact customer message and attachment.

For these eight weeks, Ava's measured business scope is **quotes**. She will receive approved inquiries, identify missing information, research the property and jurisdiction, retrieve comparables, prepare branded drafts, answer source-linked quote questions in Teams, understand revision requests, and present work for approval. The POC also establishes a reusable agent, memory, identity, file, Teams, and tool foundation so Ava can later support additional Lea & Braze workflows through separately approved capabilities.

The POC is intended to evaluate Ava across **all quote families, all jurisdictions Lea & Braze serves, and all current approved quote layouts**, rather than a narrow subset. Work begins with an inventory of those categories and at least 50 reviewed historical cases. Fifty is a starting minimum, not a cap; the set expands as needed so every major quote family, jurisdiction, and layout has representative coverage.

A historical case pairs the original inquiry and attachments with the final approved quote and corrections. Some cases configure Ava; a separate holdout set tests whether she can produce the right result without seeing the answer. After that gate passes, Ava processes an initial 15-25 new eligible inquiries in parallel. Testing continues if the incoming mix does not adequately represent major categories.

**Included:** Exchange Online intake, approved attachments, ArcGIS/public research, a controlled SMB/DFS subset, comparable retrieval, quote drafting, conversational Teams Q&A and revisions, read-only Monday.com quote context, approved memory, an authenticated review dashboard, audit history, and an approval-gated final send.

**Excluded:** company-wide rollout, all 16-17 TB of data, unrestricted file access, autonomous pricing commitments, engineering/code conclusions, full plan interpretation, Monday.com replacement or unapproved write-back, SWPPP, and unsupervised customer communication.

## Recommended Deployment and Integration

```text
Exchange Online + Teams -> Entra/Graph/Teams bot -> Hermes agent in AWS
  -> GPT-5.6 reasoning + approved memory and knowledge retrieval
  -> permissioned tools: SMB/DFS connector, ArcGIS, Monday.com, quote builder
  -> PostgreSQL workflow state and complete audit history
  -> Teams answer/revision -> named approval -> Graph sends exact package
```

| Area | POC decision |
| --- | --- |
| **Agent hosting** | Run Hermes and Ava's services in a hardened AWS environment because Lea & Braze already has AWS and a Site-to-Site connection. Use managed PostgreSQL, encrypted object storage, Secrets Manager, and logs/alerts. Only the authenticated Teams webhook is internet-facing; SMB, databases, and administration remain private. |
| **Email and identity** | IT creates a company-controlled Ava POC mailbox and adds it to the approved `info`/`RFP` distribution lists. A dedicated Entra application uses Microsoft Graph with only required mail permissions. Exchange Online RBAC scopes application access to Ava's mailbox. `Mail.Send` is enabled only for the controlled-send stage. |
| **Teams and approval** | Approved users can message Ava directly or `@Ava` in a POC chat/channel to ask quote questions or request changes. Hermes interprets the language and loads shared case context. Sending still requires an authorized, unambiguous confirmation of the exact recipient, message, attachment, and version in the Entra-authenticated review flow. |
| **Files** | Prefer a small domain-connected connector on the existing Proxmox environment. Using a dedicated AD service identity, it reads only approved SMB/DFS folders and writes only to a separate output location. It sends requested extracts over the existing private AWS connection; Hermes never receives SMB credentials or unrestricted file access. |
| **Monday.com** | Connect through a least-privilege OAuth application. During the POC Ava may read approved quote-board items, status, owner, dates, and updates for context and Q&A. Monday remains the human backlog/workload system; Ava's PostgreSQL database owns agent execution and audit state. Write-back requires a later approved tool and policy. |
| **Data controls** | Use only the approved POC subset and minimum necessary content. Region, retention, deletion, model-provider use, malware scanning, backup, and incident contacts are documented before live cases. Every file read, model call, draft, edit, approval, and send is logged. |

## Agent Runtime and Tools

**Hermes becomes Ava's primary agent runtime and Teams-facing conversational brain.** It maintains context, plans work, interprets informal language, answers questions, asks for clarification, chooses an allowed tool, and proposes memories or reusable skills. GPT-5.6 Terra supplies reasoning for inquiry interpretation, research synthesis, comparable analysis, Q&A, revisions, and drafting. After evaluation, only proven low-risk classification and extraction may move to GPT-5.6 Luna. Exact model and prompt versions are pinned during measured testing.

Python becomes a set of narrow business tools exposed to Hermes through filtered MCP interfaces: get a case, search approved comparables, request an SMB document, research a jurisdiction, build or revise a quote, read Monday context, request approval, and send the approved package. Each tool validates the Teams user, case, permissions, workflow state, inputs, and output. The model cannot change permissions, browse arbitrary files, or execute a customer-facing action directly.

<div style="page-break-after: always;"></div>

## Memory, Learning, and Expansion

Memory is layered: PostgreSQL is authoritative for cases, versions, approvals, and audit; an evaluated GBrain or equivalent knowledge layer stores source-linked company knowledge; Hermes memory stores approved preferences and lessons; and versioned skills store approved procedures. Corrections are captured, proposed as memories or skills, tested against historical cases, and activated only after human approval. Ava does not silently retrain or change pricing, jurisdiction, approval, or sending policy.

This makes Ava a genuine LLM-backed agent while retaining reliable controls. For example, `bet` is treated as acknowledgment, not approval; `change this` triggers contextual interpretation or a clarifying question; and `send it` may express intent but cannot bypass identity, version, recipient, attachment, and approval checks.

**Expansion foundation:** quotes are the only workflow evaluated in this POC. If successful, the same Teams identity, agent runtime, permission model, memory, connectors, and audit framework can later add separately approved skills for SharePoint retrieval, Monday updates, project onboarding, meeting follow-up, field reports, or other workflows without rebuilding Ava from scratch.

## Eight-Week Delivery Plan

| Weeks | Work and exit result |
| --- | --- |
| **1-2: Define and connect** | Inventory quote coverage, reviewers, baseline, historical cases, data rules, and escalation policy. Deploy AWS; configure Hermes, models, Entra/Graph, mailbox, Teams bot, dashboard sign-in, secrets, logging, private network, SMB connector, and read-only Monday access. **Exit:** IT-approved nonproduction path with sending disabled. |
| **3-4: Build the agent** | Migrate durable state; index approved templates and comparables; configure GBrain/retrieval, memory approvals, ArcGIS, quote tools, Teams Q&A/revision behavior, and model schemas. **Exit:** source-linked answers and draft packages across the historical coverage set. |
| **5-6: Evaluate and harden** | Add approval, audit, alerts, retries, duplicate/attachment checks, backup/restore, shutoff, permission tests, informal-language tests, and memory regression tests. Replay the holdout set and correct systematic failures. **Exit:** safety and quality reach the parallel-run threshold. |
| **7-8: Parallel run and decision** | Run Ava beside the existing process on an initial target of 15-25 new eligible inquiries. Measure speed, hands-on time, corrections, operating cost, and category coverage. Customer sending remains disabled unless Jim and IT authorize a monitored controlled-send window. **Exit:** scorecard, coverage gaps, risk register, operating runbook, and go/revise/stop recommendation. |

## Pass/Fail Measures

The POC proceeds beyond parallel testing only when safety and business value pass together:

- **0** unauthorized, duplicate, wrong-recipient, or wrong-attachment sends.
- At least **80%** of routine first-pass Ava packages have no material error or omission and perform no worse than the manual first pass.
- Results are reported by quote family, jurisdiction, and layout; no major category is called validated without representative historical and parallel evidence.
- Median time and human hands-on effort to a materially acceptable package are at least **50% lower** than the manual baseline.
- Median reviewer hands-on time for a routine complete package is **10 minutes or less**.
- Quote-related Teams answers and revisions are source-linked, permission-checked, and materially correct; ambiguity triggers clarification rather than an unsafe assumption.
- **100%** of measured cases preserve sources, model/prompt version, memory/skill version, output versions, human changes, approval identity, and final action.
- Uncertain jurisdiction, missing information, unsupported pricing, or out-of-scope work reliably stops for human review.

## Deliverables and Responsibilities

**POC deliverables:** AWS-hosted Hermes/Ava agent; configured mailbox, Teams Q&A/review, dashboard, SMB connector, read-only Monday quote connector, approved-memory workflow, research and quote tools; coverage matrix; historical and parallel results; security/operations runbook; audit export; scorecard; and a scoped MVP and expansion recommendation.

**Lea & Braze provides:** Jim's business decisions and final approvals; IT-created identities, permissions, network rules, POC folders, and incident contacts; timely access to at least 50 approved historical cases plus additional cases needed for representative coverage; the complete approved quote-template library; two to four pilot reviewers; and confirmation of permitted data/model use.

**Consultant provides:** implementation, migration of the demonstrated workflow into the controlled agent architecture, configuration support, testing, monitoring, documentation, weekly status, and final recommendations. Lea & Braze owns all professional and commercial decisions.

## Approval

Approval authorizes the quote-only POC and its reusable technical foundation, not a production rollout, additional business workflows, or autonomous customer communication.

| Lea & Braze approval | Date |
| --- | --- |
|  |  |
