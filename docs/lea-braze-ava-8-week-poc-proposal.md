# Ava: 8-Week Quote Agent Proof of Concept

**Prepared for:** Jim and Lea & Braze

**Date:** August 6, 2026

**Decision requested:** Approve a controlled eight-week proof of concept to determine whether Ava can reduce quote-preparation time, improve consistency, and make company knowledge easier to use while Lea & Braze keeps control of every important decision.

## Why Ava

Preparing a quote requires people to gather email attachments, search prior work, choose the right template, research the property and jurisdiction, check pricing inputs, assemble the package, and answer follow-up questions. Much of that work is repetitive, but it still requires company knowledge and judgment.

Ava is an AI-powered quote specialist that employees can work with in Microsoft Teams. She can organize each inquiry, find approved examples and templates, use ArcGIS and other approved sources, prepare a draft, explain what she used, and revise the work through normal conversation. The expected value is faster response, less time spent searching, more consistent packages, and company knowledge that can be reused instead of remaining with one person. Existing staff should be able to handle more quote demand with fewer repetitive steps while keeping human judgment where it matters.

During the POC, Ava works beside the existing process for safe comparison. If results pass, a later phase can make Ava the primary quote-preparation workflow. Quotes are the only workflow measured now, but the same Teams identity, permissions, memory, connectors, and audit foundation can later support approved SharePoint, Monday, onboarding, meeting, or field workflows. A named Lea & Braze reviewer retains professional judgment, pricing, scope, and approval of the exact customer package.

## What the POC Will Prove

The POC covers **all quote types, all jurisdictions Lea & Braze serves, and all currently approved quote layouts**. Work begins by listing those categories and reviewing at least 50 historical cases. Fifty is the starting minimum, not a limit; more are added when needed for representative coverage.

Each historical case includes the original inquiry and attachments, the final approved quote, and known corrections. Some cases are used to configure Ava. A separate holdout set, which Ava has not seen during setup, tests whether she can produce the right result independently. After passing that test, Ava prepares drafts for an initial 15-25 new inquiries while the team continues its normal process. Parallel testing continues if the live mix does not represent the major categories.

**Included:** Exchange Online intake, approved attachments, SMB/DFS network files, GBrain company-knowledge retrieval, ArcGIS/public research, quote drafting, Teams questions and revisions, read-only Monday.com quote information, approved memory and skills, a secure review page, complete audit history, and an approval-controlled final send.

**Not included:** company-wide rollout, unrestricted access to all 16-17 TB of files, autonomous pricing or scope commitments, engineering/code conclusions, full plan interpretation, Monday.com replacement or unapproved updates, SWPPP, or unsupervised customer communication.

## How Ava Works

```text
Inquiry copied to Ava mailbox -> Ava/Hermes understands and organizes it
  -> approved tools search SMB/DFS, GBrain, Monday.com, ArcGIS, and attachments
  -> Ava prepares a source-linked draft and discusses it with staff in Teams
  -> named reviewer confirms the exact recipient, message, attachment, and version
  -> Microsoft Graph sends only when the controlled-send stage is authorized
```

## Technical Design and Safeguards

| Area | Plain-language design and technical detail |
| --- | --- |
| **Agent and models** | Hermes manages Ava's conversations, context, planning, memory, and tool choice. GPT-5.6 Terra handles reasoning, research synthesis, questions, revisions, and drafting; Luna may later handle only tested, low-risk extraction or classification. OpenAI Responses use strict output schemas, and model/prompt versions stay fixed during measured tests. Restricted Python tools, connected through the Model Context Protocol (MCP), check permissions and inputs before reading data or acting. |
| **State, knowledge, and learning** | PostgreSQL records cases, versions, approvals, and audit events. GBrain stores source-linked knowledge from approved templates and historical work. Hermes memory stores approved preferences and lessons. Corrections become memories or skills only after historical testing and human approval; Ava cannot silently change pricing, jurisdiction, approval, or sending rules. |
| **AWS hosting** | IT selects its existing isolated, nonproduction AWS account and private network (VPC) pattern while preserving the private Site-to-Site connection. Reviewed infrastructure-as-code runs through a restricted role limited to tagged Ava resources, not existing workloads, IAM, VPN, or routing. The environment includes PostgreSQL, encrypted storage, Secrets Manager, budgets, logs, and alerts. Only the authenticated Teams message endpoint is public. |
| **Microsoft 365 and Teams** | IT creates Ava's company mailbox, adds it to approved inquiry lists, and approves a dedicated Entra application. Microsoft Graph, Microsoft 365's supported API, is limited to that mailbox. Approved users can message Ava directly or `@Ava` in the POC Teams space, and the review page uses Entra sign-in. Conversation can request answers and revisions; Microsoft's send permission remains disabled until a controlled-send test is explicitly approved. |

<div style="page-break-after: always;"></div>

## Connections and Data Controls

| Area | Plain-language design and technical detail |
| --- | --- |
| **Company files** | A small connector runs in the existing Proxmox environment using a dedicated Active Directory identity. It can read only approved SMB/DFS folders and write only to a separate output folder. It exchanges requested information through one narrow, IT-approved connection. AWS does not join the company domain or mount the full file share, and Hermes never receives SMB credentials. |
| **Monday.com and research** | A least-privilege Monday application reads the approved quote boards, ownership, dates, status, columns, and updates for context and questions. Monday remains the team's backlog/workload system; Ava's database owns agent execution and audit history. Monday write-back requires separate approval. ArcGIS and approved public sources support property and jurisdiction research. |
| **Data protection** | Only the approved POC data set and minimum necessary content are used. Before live cases, IT and leadership approve the cloud region, model provider, retention, deletion, malware scanning, backup, and incident contacts. Every mailbox action, file read, Monday query, model call, draft, correction, approval, and send is logged. |

## Eight-Week Delivery Plan

The consultant owns design, coding, deployment, integration, testing, monitoring, and documentation. IT does not build Ava; it performs the company-controlled AWS, Microsoft, network, AD, file, and Monday approvals. To reduce interruptions, the consultant provides one setup checklist before kickoff, tracks access issues in one place, and batches reviewer questions into scheduled sessions. The target is two IT working sessions in weeks 1-2, followed by exception support only.

| Weeks | Work, ownership, and proof before moving on |
| --- | --- |
| **1-2: Connect everything safely** | **Consultant:** map quote coverage and data flow; deploy Ava, Hermes, PostgreSQL, GBrain, storage, secrets, logs, and the review page in the AWS location IT selects; prepare every connector. **IT:** approve the restricted AWS role and existing private route; create the mailbox/Entra application, Teams pilot, read-only file identity/output folder, and read-only Monday access. **Reviewers:** identify rules, escalation points, and historical cases. **Ready when:** Exchange intake works; every pilot user can reach Ava; every approved SMB/DFS root and supported file type can be read but not changed; output is isolated; every approved Monday board/column/update type can be read but not changed; ArcGIS, model, and review access work; logs and credential revocation work; customer sending is disabled. |
| **3-4: Build the complete quote behavior** | **Consultant:** move case state to PostgreSQL; load approved templates and development cases into GBrain with links to their sources; configure retrieval, controlled learning, ArcGIS research, quote tools, and Teams questions/revisions. **Reviewers:** validate source choice, templates, research, pricing inputs, draft structure, and answers in scheduled batches. **Ready when:** development cases cover every populated quote type, jurisdiction, and layout category; Ava completes intake through draft, uses SMB, Monday, and public information correctly, cites its evidence, asks when information is missing, and never contacts customers. Any missing coverage is listed clearly. |
| **5-6: Prove quality, security, and recovery** | **Consultant:** run untouched holdout cases and correct repeatable failures; test every connector's permissions, exact-version approval, duplicate/attachment protection, retries, audit logs, alerts, backup/restore, emergency shutoff, unclear Teams requests, and memory changes. **Reviewers:** score drafts, record corrections, and approve or reject proposed learning in batches. **Ready when:** quality meets the agreed threshold across represented categories; prohibited reads, writes, and unauthorized actions fail; failures alert and recover correctly; restored state is complete; and Ava is ready for parallel work. |
| **7-8: Compare Ava with live work** | **Team:** continue the normal process while Ava receives copies of an initial 15-25 eligible inquiries and independently prepares drafts. Testing continues if the live mix misses major categories. **Consultant:** monitor every case and report time, hands-on effort, corrections, cost, and results by quote type, jurisdiction, and layout. Ava sends nothing unless Jim and IT separately approve a monitored send test. **Ready when:** Lea & Braze has a final scorecard, integration-reliability results, coverage gaps, risk register, operating runbook, and a go, revise, or stop recommendation. |

## Success Measures

The POC advances only when business value and safety pass together:

- **0** unauthorized, duplicate, wrong-recipient, or wrong-attachment sends.
- At least **80%** of routine first drafts have no material error or omission and perform no worse than the manual first draft.
- Results are reported by quote type, jurisdiction, and layout; no major category is called validated without representative evidence.
- Median elapsed time and staff hands-on effort to an acceptable package are at least **50% lower** than the manual baseline.
- Median reviewer hands-on time for a routine complete package is **10 minutes or less**.
- Teams answers and revisions are source-linked, permission-checked, and materially correct; unclear requests produce a question instead of an unsafe assumption.
- **100%** of measured cases preserve sources, model/prompt/memory versions, drafts, human changes, reviewer identity, and final action.
- Missing information, uncertain jurisdiction, unsupported pricing, or out-of-scope work reliably stops for human review.

## Deliverables and Responsibilities

**Delivered:** working AWS-hosted Hermes/Ava agent; PostgreSQL and GBrain; configured mailbox, Teams, review page, SMB connector, read-only Monday connector, approved-memory process, research and quote tools; integration and quote-coverage checklists; historical and parallel results; security/operations runbook; audit export; scorecard; and a recommended next phase.

**Lea & Braze provides:** Jim's business decisions and final approvals; IT-created identities, permissions, network rules, POC folders, and incident contacts; at least 50 approved historical cases plus any needed for coverage; the approved template library; two to four pilot reviewers; and approval of permitted data/model use.

**Consultant provides:** implementation, deployment, integration, testing, monitoring, documentation, weekly status, and final recommendations. Lea & Braze retains every professional and commercial decision.

**Approval:** Approval authorizes the quote-only POC and its reusable foundation, not production rollout, additional workflows, or autonomous customer communication. Lea & Braze approval: ____________________ Date: __________
