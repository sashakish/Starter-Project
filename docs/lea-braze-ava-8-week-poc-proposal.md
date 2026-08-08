# Ava: 8-Week Quote Agent Proof of Concept

**Prepared for:** Jim and John (IT), Lea & Braze

**Date:** August 7, 2026

**Review version:** Scope and deployment approach; commercial terms to follow.

**Review requested:** Confirm that this eight-week POC scope and controlled deployment approach should move to commercial discussion. Ava is intended to reduce quote turnaround and senior staff effort, increase capacity to pursue more work, and preserve company knowledge. Lea & Braze retains final approval of every price, scope, and completed quote.

## Business Case - Planning Assumption

Meeting records show approximately **763 quotes in the prior year, or about 64 per month**, and **495 quotes already recorded in 2026** at the August 3 IT meeting. The discussion indicated that Jim and Pete prepare much of this work because it depends on their experience. That volume, the historical archive, and the repeatable workflow provide strong evidence that Ava has meaningful work to automate.

**Planning assumption:** Saving one senior hour per quote would release roughly **64 senior hours, or eight workdays, each month** and create capacity to answer more opportunities sooner and potentially win more business. Exact current effort and revenue impact are not yet confirmed; Jim will confirm a rough baseline before the final SOW, and the POC will measure the actual result. This is an assumption to test, not a guaranteed outcome.

## Why Ava

Ava is a powerful, always-available digital employee that staff work with in Microsoft Teams. She receives approved inquiries around the clock, checks completeness, asks customers only for required missing information, searches approved company knowledge and tools in seconds, prepares source-linked priced drafts, explains her evidence, and revises work through normal conversation. People retain professional and commercial judgment while Ava handles repetitive search, research, follow-up, and document assembly at software speed.

During the POC, Ava works beside the existing process for safe comparison. Quotes are the only workflow measured now, but the same Teams identity, permissions, memory, connectors, and audit foundation can later support other approved company workflows.

## Scope and Evidence

Ava is designed for **all known quote types, all jurisdictions Lea & Braze serves, and all currently approved layouts**. More than 50 historical cases, plus additional cases where coverage is thin, are divided between configuration and an untouched holdout test. An initial 15-25 new inquiries then test live operation beside the current process.

The final scorecard will distinguish **historically tested** coverage from **live-validated** coverage. A category is not called live-validated unless it appears in the live sample; if major categories are missing, cases are added or the measured run continues. This makes the eight-week result honest about long-tail coverage.

**Included:** Exchange Online intake, approved attachments, SMB/DFS files, GBrain knowledge retrieval, versioned Pricing Memory, ArcGIS/public research, automatic missing-information requests, quote drafting, Teams questions/revisions, read-only Monday.com project information, approved learning, a secure review page, complete audit history, and reviewer-approved final quote sending.

**Not included:** company-wide rollout, unrestricted access to all 16-17 TB of files, Ava changing approved pricing rules or committing pricing/scope without reviewer approval, professional engineering judgments, code-compliance decisions, complete construction-plan review, Monday.com replacement or unapproved updates, SWPPP, or customer communication beyond necessary information requests and reviewer-approved final quotes.

## Ava's POC Quote Workflow

```text
Inquiry copied to Ava mailbox -> Ava organizes it and checks completeness
  -> if information is missing, Ava asks the customer only for what is required
  -> approved tools search company files, knowledge, pricing, Monday, and ArcGIS
  -> Ava prepares a sourced draft and revises it with staff in Teams
  -> reviewer approves price, scope, recipient, message, file, and version -> final quote sends
```

## Safety and Success Gates

- **100%** of completed quotes require named-reviewer approval; **0** unauthorized, duplicate, wrong-recipient, or wrong-attachment final sends.
- Automatic customer messages are limited to tested requests for required missing information; uncertain scope, jurisdiction, or pricing routes to a person.
- At least **80%** of routine drafts are approval-ready on first review with no material error or omission; all others remain internal until corrected.
- A measured baseline is established first. At least **50%** lower turnaround and staff effort, plus **10 minutes or less** reviewer time for routine complete quotes, are minimum POC gates rather than promised results or performance ceilings.
- Results are reported by quote type, jurisdiction, and layout, with historical and live validation clearly separated.
- **100%** of measured cases preserve sources, versions, drafts, changes, reviewer identity, and final action.

<div style="page-break-after: always;"></div>

## Technical Plan for John and IT

| Area | Plain-language design and technical detail |
| --- | --- |
| **Agent, models, and tools** | Hermes manages Ava's context, planning, memory, and tool choice. GPT-5.6 Terra establishes the reasoning and drafting baseline; Luna may later handle only proven low-risk extraction or classification. The OpenAI Responses API uses strict schemas and fixed model/prompt versions during measured tests. Custom-built tools connect through MCP and check permissions before reading data or acting. |
| **Knowledge, learning, and pricing** | PostgreSQL records cases, versions, approvals, and audit events. GBrain stores source-linked knowledge from approved work; Hermes stores approved preferences and lessons. A versioned Pricing Memory holds rates, minimums, jurisdiction differences, exceptions, effective dates, and sources. Ava shows pricing assumptions, cannot silently change a rule, and every final price requires approval. Learning changes require testing and human approval. |
| **AWS and company files** | IT selects an isolated nonproduction area in its existing AWS environment and private network, preserving the Site-to-Site connection. A connector in Proxmox uses a dedicated Active Directory identity to read only approved SMB/DFS folders and write only to a separate output folder. AWS does not join the domain or mount the full share. Restricted roles, encryption, Secrets Manager, budgets, logs, alerts, backup, and shutoff controls protect the POC. |
| **Microsoft 365 and Teams** | IT creates Ava's mailbox and dedicated Entra application; Microsoft Graph is restricted to that mailbox. Approved users can message or `@Ava` in the POC Teams space. IT also provides the consultant account and a private Ava POC Development channel with John and designated IT staff. After testing, Ava may request missing customer information automatically; final quotes remain blocked until named approval. |
| **Monday, research, and protection** | A least-privilege Monday application reads approved project information; write-back requires separate approval. ArcGIS and approved public sources support property and jurisdiction research. Only the approved POC data set is used, with agreed retention and deletion. Every mailbox action, file read, Monday query, model call, draft, correction, approval, and send is logged. |

## Eight-Week Delivery Plan

**Client-effort target:** Jim handles scope, commercial, and final go/no-go decisions; John/IT joins up to two optional remote setup sessions; and two to four reviewers share a batched queue targeted at no more than two total staff-hours per week in weeks 3-8. After access is granted, the consultant organizes and loads the historical cases and performs all implementation work.

| Weeks | Work and proof before moving on |
| --- | --- |
| **1-2: Connect safely** | **Consultant:** map coverage and baseline; deploy the Ava stack in IT-selected AWS; prepare connectors and one setup checklist. **IT:** approve the restricted AWS/private route; create mailbox/Entra, Teams spaces and consultant account, read-only file/output identities, and Monday access. **Reviewers:** confirm quote, pricing, and escalation rules and point to representative cases. **Ready when:** intake and approved connections work, output is isolated, access can be revoked, and external sending remains off while follow-up rules are tested. |
| **3-4: Build quote behavior** | **Consultant:** organize and load approved cases, templates, and Pricing Memory; configure retrieval, learning, pricing, ArcGIS, quote, and Teams tools. **Reviewers:** validate sources, pricing, drafts, and answers in batches. **Ready when:** development cases cover every populated category; Ava produces cited priced drafts, automatically requests only required missing information, and cannot send a final quote without approval. |
| **5-6: Prove quality and safety** | **Consultant:** run untouched holdout cases; correct repeatable failures; test permissions, automatic questions, final approval, duplicates, attachments, retries, audit, alerts, backup/restore, shutoff, unclear Teams requests, and memory changes. **Reviewers:** score drafts and approve or reject proposed learning. **Ready when:** safety and quality gates pass across represented categories and recovery works. |
| **7-8: Compare live work** | **Team:** continue normal work while Ava independently handles an initial 15-25 eligible inquiries. **Consultant:** report turnaround, staff effort, corrections, cost, added capacity, and results by category. Tested missing-information questions may send without case approval; every final quote requires named approval. **Ready when:** Lea & Braze receives the scorecard, historical-versus-live coverage, reliability results, risk register, runbook, and go/revise/stop recommendation. |

## Deliverables and Responsibilities

**Delivered:** working AWS-hosted Ava agent; configured mailbox, Teams and review experience; PostgreSQL, GBrain, Pricing Memory, SMB and Monday connectors, research/pricing/quote tools, approved-learning process, audit export, test results, coverage report, security/operations runbook, scorecard, and recommended next phase.

**Lea & Braze provides:** Jim's decisions; John/IT approvals, identities, permissions, network rules, Teams spaces, and incident contact; access to approved historical cases, templates, rate sheets, pricing rules, and known exceptions; two to four reviewers; and approval of permitted data/model use. The consultant prepares the historical data after access is granted.

**Consultant provides:** design, implementation, deployment, integration, testing, monitoring, documentation, weekly status, and final recommendations. Lea & Braze retains every professional and commercial decision.

## Next Step and Final SOW

This review version does **not** authorize implementation. Jim and John first confirm the scope and technical approach. Engagement pricing, billing terms, and the start date are then discussed in person and inserted into this same document. That updated version becomes the final Statement of Work, and work begins only after it is signed.
