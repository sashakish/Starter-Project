# Ava POC IT Meeting Answers

Source: `2026-08-03-ava-poc-full-meeting-transcript.md`

This is a transcript-derived working record, not final IT approval. The source is an automated transcript and contains recognition errors. `Confirmed` means the meeting directly answered the question. `Partial` means part of the answer is supported, but a follow-up is still required. `Not answered` means the transcript does not provide a reliable answer.

## Email and Teams

### 1. Where is the project quote inquiry mailbox hosted?

**Status: Confirmed**

Lea & Braze's email is fully hosted in **Exchange Online**. The company previously ran on-premises Exchange and then a hybrid setup, but moved all mailboxes online around 2019. Quote inquiries do not enter through one mailbox: customers may email individual employees, the general `info` address, or the `RFP` address.

Transcript evidence: lines 19-43.

### 2. Which inbox receives quote requests, and what type is it?

**Status: Confirmed, with exact addresses to verify**

The two main general entry points are the `info` and `RFP` email addresses. They are **distribution lists**, not shared mailboxes. The list shown during the meeting appeared to have about 13 members, each receiving a copy. Some inquiries bypass those lists and go directly to Jim, a project manager, or another employee.

The automated transcript does not preserve the exact spelling of the email domain reliably, so IT should provide the exact SMTP addresses before configuration.

Transcript evidence: lines 20-36.

### 3. Can IT create a separate POC mailbox and later an Ava mailbox?

**Status: Partial; accepted in principle, pending Jim's approval**

John proposed creating a mailbox in the company's Exchange Online environment and adding it as a member of the relevant distribution list so it receives copies while existing delivery remains unchanged. The POC would observe incoming work only and would not send anything. John said he would run this by Jim.

A dedicated mailbox or service identity was also accepted as the likely pattern. The meeting did not establish the required Microsoft 365 license, setup time, or approval for later outbound sending and replies.

Transcript evidence: lines 137-152.

### 4. Does the proposed connection and sign-in method fit the current setup?

**Status: Partial**

The dedicated Exchange Online mailbox/service-identity pattern fits the environment. Exchange Online includes native Microsoft Graph support, so Lea & Braze does not need to install or enable a separate Graph connector. The statement in the meeting that the company has no existing Graph integration means that no Ava-specific Graph application and access configuration exists yet; it does not mean that Exchange Online lacks Graph support.

Working implementation: IT creates the company mailbox, adds it to the approved distribution lists, registers a dedicated Ava application in Entra ID, grants only the required Microsoft Graph mail permissions and admin consent, and configures an IT-approved credential. Exchange Online RBAC for Applications should limit Ava's access to the approved mailbox. The meeting did not finalize or approve those permissions, credentials, or access rules.

Technical references: [Microsoft Graph mail API](https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview?view=graph-rest-1.0), [Microsoft identity permissions and consent](https://learn.microsoft.com/en-us/entra/identity-platform/permissions-consent-overview), and [Exchange Online RBAC for Applications](https://learn.microsoft.com/en-us/exchange/permissions-exo/application-rbac).

Transcript evidence: lines 39-55 and 148-152.

### 5. Are there email constraints such as forwarding blocks, limits, disclaimers, spam rules, or retention?

**Status: Not answered**

No special email constraint was identified during the meeting. The proposed design avoids external auto-forwarding by adding a company mailbox directly to the distribution lists. Attachment limits, signatures, disclaimers, spam protection, journaling, and retention were not discussed and still require confirmation from IT.

### 6. Is Teams in the same tenant, and can Ava use a limited Team or channel?

**Status: Partial**

Teams is part of the company's Microsoft 365 environment and appears to be in the same tenant as Exchange Online, although this was implied rather than stated directly. The participants agreed that Ava should have a dedicated, approved Teams space where it can read and write and where selected POC users can interact with it.

The company currently relies more on group chats than Teams channels, even though John previously created departmental and office-wide Teams/channels. The POC may therefore require a new channel and some user adoption work. Tenant admin steps, app registration or bot approval, channel privacy, and any additional licensing were not resolved.

Transcript evidence: lines 170-190.

## Files

### 7. Where do historical inquiries, quotes, templates, pricing references, and project files live?

**Status: Confirmed**

Most project content is stored on an **on-premises SMB share exposed through a DFS namespace**. Historical quotes are in an SMB folder called `quotes`, and broader project content is organized by project number. Lea & Braze is slowly moving suitable content into SharePoint and OneDrive, but less than 5% of its data is currently in SharePoint.

AutoCAD working files are expected to remain on SMB because the SharePoint workflow does not work well for them. Quotes, PDFs, and other customer-facing derivatives are better candidates for SharePoint.

Transcript evidence: lines 195-215 and 384-388.

### 8. What are the SMB/DFS paths, server details, and AD domain?

**Status: Partial**

The meeting confirmed SMB through a DFS namespace and an on-premises Active Directory environment. It did **not** capture the UNC/DFS paths, file-server or NAS product and version, DFS namespace name, or AD DNS domain. IT must provide those values before Ava's file connector can be configured.

Transcript evidence: lines 195-202.

### 9. How do engineers access files remotely or in the field?

**Status: Confirmed**

Engineers using company Windows laptops connect with **Cisco AnyConnect VPN** and then access the normal internal network/DFS/SMB paths. VPN logs can show connection and access activity.

Field crews also use Android devices. Accessing SMB over VPN from those devices is difficult to configure and manage, which is one reason Lea & Braze is moving field-appropriate files to SharePoint for easier cloud access.

Transcript evidence: lines 198 and 238-247.

### 10. Can IT create an approved read-only POC folder and a separate output location?

**Status: Partial; explicit approval still required**

The meeting assumed Ava would receive a limited identity and authenticated VPN access to approved on-premises content. That supports a least-privilege POC folder design, but John did not explicitly confirm that IT will create the folder, make the input read-only, or provide a separate write location.

Required follow-up: identify the approved file subset, create a read-only input permission for Ava, create a separate output location, and confirm that Ava cannot modify source files.

Transcript evidence: lines 217-241 and 268-273.

### 11. What file types, sizes, volume, scanning, retention, backup, and sync should be expected?

**Status: Partial**

The total environment contains about **16-17 TB**. Mentioned file types include AutoCAD files, PDFs, quotes, and other project records. Content is organized around a project number used consistently across the network. The transcript says there were about 495 quotes in 2026 at the time of the meeting and about 762-763 in the previous year.

Individual file-size ranges, the exact POC subset size, malware scanning, retention, backups, and existing file-sync controls were not answered. SharePoint migration is underway, but it is not a general SMB synchronization solution.

Transcript evidence: lines 207-215, 251-256, and 384-388.

## Azure and Network

### 12. Is the office connected to Azure by Site-to-Site VPN or ExpressRoute?

**Status: Confirmed; the answer changes the proposed hosting assumption**

No Azure private-network connection was identified. Lea & Braze already has a **Site-to-Site connection to AWS**, and AWS hosts its current cloud VMs. Azure is currently used mainly for Microsoft 365 licensing, Entra/user management, and related administration; the company does not have Azure compute infrastructure set up.

The meeting therefore leaned toward AWS as the easiest POC host. If Ava must run in Azure, a new Site-to-Site VPN plus private DNS and any required AD reachability would need to be designed and approved.

Transcript evidence: lines 82-90, 259-260, and 273-285.

### 13. What network rules apply between Lea & Braze and the cloud environment?

**Status: Partial**

John said IT can create the firewall and access rules required by the POC. Access to on-premises SMB must travel through an authenticated VPN/private tunnel. The existing AWS Site-to-Site connection may make AWS the simplest host.

The meeting did not specify outbound HTTPS rules, proxies, allowlists, static addresses, DNS forwarding, certificates, inbound-access restrictions, ports, or exact source and destination networks. These should be documented before deployment; SMB should not be exposed publicly.

Transcript evidence: lines 217-218, 235-261.

## Accounts, Data, and Support

### 14. Are on-premises AD and Entra ID connected, and how are service identities managed?

**Status: Partial**

Yes. User identities are managed in **on-premises Active Directory** and synchronized to Entra ID with Microsoft's directory-sync tooling. Only two IT staff members have Azure administrative access. The discussion supported giving the POC a dedicated, limited credential rather than a person's account.

The meeting did not define the exact service-account process, Graph tenant-consent process, certificate versus secret choice, secret rotation, MFA treatment, or Conditional Access policies. Those remain IT design and approval items.

Transcript evidence: lines 57-62, 264-273, and 363-364.

### 15. Are there data types that cannot enter the cloud or an external AI service?

**Status: Not formally answered**

No prohibited data categories were identified in the meeting. The discussion assumed that approved historical quotes and related customer, project, location, and pricing information could be analyzed and transformed into a structured cloud index for the POC. That assumption is **not the same as security or legal approval**.

IT or company leadership still needs to explicitly approve which files may leave the on-premises share, which external AI providers may receive content, the allowed cloud account and region, masking requirements, retention period, deletion procedure, and whether data may be used for model training. Until then, only a specifically approved POC subset should be used.

Transcript evidence: lines 364-401 and 446.

### 16. Does Lea & Braze need audit logs or alerts, and who handles incidents?

**Status: Partial; alerts are desired, contact procedure is open**

Yes. John specifically wanted proactive alerts for unusual access or large data-copy activity. The company can inspect SMB access logs, and VPN logs can show remote access, but it does not currently have proactive detection for this scenario. The meeting also referenced a previous incident in which company templates or standards were taken and the company learned about it from an outside party.

The POC should log mailbox, file, VPN, model, administrative, and output actions and alert Lea & Braze on unusual volume or behavior. A notification email, named incident contact, escalation path, and rapid-disable procedure still need to be agreed. John and the second IT administrator are the apparent operational owners, but the transcript did not formally designate an emergency contact.

Transcript evidence: lines 239-241, 296-300, and 430-446.

### 17. Are there licenses, approvals, costs, or blockers that may add time?

**Status: Partial**

The main approval is **Jim's authorization**. John planned to review the proposal with him. The POC should be a limited release with designated evaluators before any broader rollout. John also wanted the final POC proposal to describe the required data and access so he and Jim can approve it.

The working assumption was that Lea & Braze would not incur a meaningful new infrastructure charge during the initial POC, but the exact AWS/Azure, AI-model, Microsoft 365, mailbox, and Teams licensing costs were not finalized. Lea & Braze obtains Microsoft licensing through Trusted Tech. The conversation mentioned an estimated six-to-eight-week POC configuration period, while the test duration and success criteria remain separate open decisions.

Known dependencies are Jim's approval, mailbox and Entra setup, a Teams space, approved SMB permissions, cloud-to-office VPN/firewall configuration, a data-handling decision, named POC evaluators, and an incident-notification protocol. The company budget was not known during the meeting.

Transcript evidence: lines 65-66, 102-130, 291-302, 329-351, and 409-450.

## Remaining IT Confirmations

The transcript provides a usable working answer for every question, but the following details must still be confirmed before implementation:

1. Exact `info` and `RFP` SMTP addresses and distribution-list membership.
2. Mailbox license, Graph application registration, tenant consent, and authentication method.
3. Teams tenant/channel details, app permissions, and licensing.
4. DFS/UNC paths, file-server details, AD domain, approved POC folder, permissions, and output location.
5. POC file subset, size profile, malware scanning, retention, backup, and synchronization controls.
6. Final AWS-versus-Azure hosting decision and the exact VPN, routing, DNS, firewall, and certificate design.
7. Service-identity lifecycle, MFA/Conditional Access treatment, secrets, certificates, and rotation.
8. Written approval for customer/project/pricing data, external AI use, region, masking, retention, and deletion.
9. Audit-log recipients, alert thresholds, incident contact, and emergency shutdown procedure.
10. Jim's approval, named POC evaluators, budget, licenses, test duration, and success criteria.
