# Ava: 8-Week Quote Agent Proof of Concept

**Prepared for:** Jim and Lea & Braze

**Date:** August 6, 2026

**Decision requested:** Approve an eight-week proof of concept to deliver and validate Ava, a secure, always-available digital employee built to transform quote preparation: dramatically reduce turnaround and staff effort, increase capacity and consistency across every quote type and jurisdiction, and turn Lea & Braze's historical work into reusable company knowledge, while the company retains final approval of pricing, scope, and every completed quote sent to a customer.

## Why Ava

Preparing a quote requires people to gather email attachments, search prior work, choose the right template, research the property and jurisdiction, check pricing inputs, assemble the package, and answer follow-up questions. Much of that work is repetitive, but it still requires company knowledge and judgment.

Ava is a powerful, always-available digital employee that staff work with in Microsoft Teams. She can receive approved inquiries around the clock, search years of company knowledge and trusted sources in seconds, prepare and revise complete quote packages, explain her evidence, and learn from reviewed corrections. By handling repetitive search, research, assembly, and follow-up at software speed, Ava can dramatically reduce turnaround and expand quote capacity without matching headcount growth. People retain professional and commercial judgment, while company knowledge becomes consistent, reusable, and available beyond any one person.

During the POC, Ava works beside the existing process for safe comparison. If results pass, a later phase can make Ava the primary quote-preparation workflow. Quotes are the only workflow measured now; the same Teams identity, permissions, memory, connectors, and audit foundation can later support approved SharePoint, Monday, onboarding, meeting, or field workflows. A named Lea & Braze reviewer retains professional judgment and approves the final pricing, scope, and customer package.

## What the POC Will Prove

The POC covers **all quote types, all jurisdictions Lea & Braze serves, and all currently approved quote layouts**. Work begins by listing those categories and reviewing more than 50 historical cases. Additional cases are added whenever needed for representative coverage.

Each historical case includes the original inquiry and attachments, the final approved quote, and known corrections. Some cases are used to configure Ava. A separate holdout set, which Ava has not seen during setup, tests whether she can produce the right result independently. After passing that test, Ava prepares drafts for an initial 15-25 new inquiries while the team continues its normal process. Parallel testing continues if the live mix does not represent the major categories.

**Included:** Exchange Online intake, approved attachments, SMB/DFS network files, GBrain company-knowledge retrieval, a versioned Pricing Memory and calculation tool, ArcGIS/public research, automatic requests for missing quote information, quote drafting, Teams questions and revisions, read-only Monday.com project information, approved memory and skills, a secure review page, complete audit history, and a reviewer-approved final quote send.

**Not included:** company-wide rollout, unrestricted access to all 16-17 TB of files, Ava changing approved pricing rules or committing pricing/scope without reviewer approval, professional engineering judgments, code-compliance decisions, complete construction-plan review, Monday.com replacement or unapproved updates, SWPPP, or customer communication beyond necessary information requests and reviewer-approved final quotes.

## How Ava's POC Quote Workflow Works

```text
Inquiry copied to Ava mailbox -> Ava organizes it and checks completeness
  -> if information is missing, Ava asks the customer only for what is required
  -> approved tools search SMB/DFS, GBrain, Pricing Memory, Monday, and ArcGIS
  -> Ava prepares a sourced draft and revises it with staff in Teams
  -> reviewer approves price, scope, recipient, message, file, and version -> Microsoft Graph sends final quote
```

## Technical Design and Safeguards

| Area | Plain-language design and technical detail |
| --- | --- |
| **Agent and models** | Hermes manages Ava's conversation context, planning, memory, and tool choice. GPT-5.6 Terra handles reasoning, research synthesis, questions, revisions, and drafting; Luna may later handle only proven low-risk extraction or classification. The OpenAI Responses API uses strict output schemas, with model and prompt versions fixed during measured tests. Custom-built tools connect through the Model Context Protocol (MCP) and check permissions and inputs before reading data or acting. |
| **State, knowledge, and learning** | PostgreSQL records cases, versions, approvals, and audit events. GBrain stores source-linked knowledge from approved templates and historical work. Hermes memory stores approved preferences and lessons. Corrections become memories or skills only after historical testing and human approval; Ava cannot silently change pricing, jurisdiction, approval, or sending rules. |
| **Pricing Memory** | PostgreSQL stores the approved pricing catalog: service items, rates, minimums, jurisdiction differences, exceptions, effective dates, and source documents. GBrain provides historical comparable context. Ava maps the requested scope to candidate items, and a custom-built pricing tool calculates the price and shows the reviewer its rate sources and assumptions. Approved corrections can propose a versioned update; Ava cannot invent or silently change a rate, and a person approves every final price. |
| **AWS hosting** | IT selects its existing isolated, nonproduction AWS account and private network (VPC) pattern while preserving the private Site-to-Site connection. Reviewed infrastructure-as-code runs through a restricted role limited to tagged Ava resources, not existing workloads, IAM, VPN, or routing. The environment includes PostgreSQL, encrypted storage, Secrets Manager, budgets, logs, and alerts. Only the authenticated Teams message endpoint is public. |
| **Microsoft 365 and Teams** | IT creates Ava's mailbox and dedicated Entra application; Microsoft Graph is limited to that mailbox. Approved users can message Ava or `@Ava` in the POC Teams space, and the review page uses Entra sign-in. Once tested, Ava may automatically request required missing information; each final quote remains blocked until a named reviewer approves its exact content and version. |

<div style="page-break-after: always;"></div>

## Connections and Data Controls

| Area | Plain-language design and technical detail |
| --- | --- |
| **Company files** | A connector in the existing Proxmox environment uses a dedicated Active Directory identity. It reads only approved SMB/DFS folders, writes only to a separate output folder, and exchanges requests through one IT-approved connection. AWS does not join the company domain or mount the full share; Hermes never receives SMB credentials. |
| **Monday.com and research** | A least-privilege Monday application reads approved project boards, ownership, dates, status, columns, and updates. Monday remains the team's backlog/workload system; Ava's database owns agent execution and audit history. Write-back requires separate approval. ArcGIS and approved public sources support property and jurisdiction research. |
| **Data protection** | Only the approved POC data set and minimum necessary content are used. Before live cases, IT and leadership approve the cloud region, model provider, retention, deletion, malware scanning, backup, and incident contacts. Every mailbox action, file read, Monday query, model call, draft, correction, approval, and send is logged. |

## Eight-Week Delivery Plan

The consultant owns design, coding, deployment, integration, testing, monitoring, and documentation. IT only performs company-controlled AWS, Microsoft, network, AD, file, and Monday approvals. The consultant provides one setup checklist, tracks access issues in one place, and batches questions. If needed, up to two optional remote IT sessions are available in weeks 1-2, followed by exception support only.

| Weeks | Work, ownership, and proof before moving on |
| --- | --- |
| **1-2: Connect everything safely** | **Consultant:** map coverage and data flow; deploy the Ava stack in IT-selected AWS; prepare connectors. **IT:** approve the restricted AWS role/private route; create the mailbox/Entra application, Teams pilot, consultant Teams account and private Ava POC Development channel with John and designated IT staff, read-only file identity/output folder, and read-only Monday access. **Reviewers:** confirm quote, pricing, and escalation rules; approve sources; select historical cases. **Ready when:** intake, pilot access, approved files/Monday data, ArcGIS, models, pricing, review, logs, and credential revocation work; output is isolated; external sending remains off while follow-up rules are tested. |
| **3-4: Build the complete quote behavior** | **Consultant:** load case state and Pricing Memory into PostgreSQL; load approved templates/cases into GBrain; configure retrieval, learning, pricing, ArcGIS, quote, and Teams tools. **Reviewers:** validate sources, templates, research, pricing, drafts, and answers in batches. **Ready when:** development cases cover every populated quote type, jurisdiction, and layout; Ava produces cited priced drafts, uses approved sources, automatically requests only required missing information, and cannot send a final quote without reviewer approval. Gaps are listed. |
| **5-6: Prove quality, security, and recovery** | **Consultant:** run holdout cases; correct repeatable failures; test connector permissions, automatic information requests, final-quote approval, duplicate/attachment protection, retries, audit, alerts, backup/restore, shutoff, unclear Teams requests, and memory changes. **Reviewers:** score drafts and approve or reject proposed learning in batches. **Ready when:** quality passes across represented categories; prohibited actions fail; alerts and recovery work; restored state is complete; and Ava is ready for parallel work. |
| **7-8: Compare Ava with live work** | **Team:** continue normal work while Ava independently handles an initial 15-25 eligible inquiries; continue if major categories are missing. **Consultant:** report time, hands-on effort, corrections, cost, and results by quote type, jurisdiction, and layout. After follow-up rules pass testing, Ava may ask focused missing-information questions without case-by-case approval; every final quote still requires named-reviewer approval. **Ready when:** Lea & Braze receives the scorecard, reliability results, coverage gaps, risk register, runbook, and go, revise, or stop recommendation. |

## Success Measures

The POC advances only when business value and safety pass together:

- **0** unauthorized, duplicate, wrong-recipient, or wrong-attachment sends.
- At least **80%** of routine first drafts have no material error or omission and perform no worse than the manual first draft.
- Results are reported by quote type, jurisdiction, and layout; no major category is called validated without representative evidence.
- Median elapsed time and staff hands-on effort to an acceptable package are reduced substantially; **50% is the minimum pass threshold, not the performance target**.
- Median reviewer hands-on time for a routine complete package is **10 minutes or less**.
- Teams answers and revisions are source-linked, permission-checked, and materially correct; unclear requests produce a question instead of an unsafe assumption.
- **100%** of measured cases preserve sources, model/prompt/memory versions, drafts, human changes, reviewer identity, and final action.
- Missing required information produces a focused customer question without reviewer approval; uncertain jurisdiction, unsupported pricing, or out-of-scope work routes to human review.

## Deliverables and Responsibilities

**Delivered:** working AWS-hosted Ava agent; PostgreSQL, GBrain, and versioned Pricing Memory; configured mailbox, Teams, review page, SMB connector, read-only Monday connector, approved-memory process, research, pricing, and quote tools; integration and quote-coverage checklists; historical and parallel results; security/operations runbook; audit export; scorecard; and a recommended next phase.

**Lea & Braze provides:** Jim's business decisions and final approvals; IT-created identities, permissions, network rules, POC folders, and incident contacts; an approved consultant Teams account and private Ava POC Development channel with John and designated IT staff; more than 50 approved historical cases, expanded as needed for representative coverage; approved templates, rate sheets, pricing rules, and known exceptions; two to four pilot reviewers; and approval of permitted data/model use.

**Consultant provides:** implementation, deployment, integration, testing, monitoring, documentation, weekly status, and final recommendations. Lea & Braze retains every professional and commercial decision.

**Commercial terms:** Engagement pricing will be discussed in person and documented separately.

**Approval:** Approval authorizes the quote-only POC and its reusable foundation, not production rollout, additional workflows, or unreviewed final quotes or commercial commitments. Lea & Braze approval: ____________________ Date: __________
