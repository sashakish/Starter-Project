# Questions for John: Ava POC Setup

Hi John,

Ava is the name of a software-based digital worker I'm proposing to run in Azure for Lea & Braze. For this POC, she would work alongside the current quote process by receiving copies of all project inquiries, gathering approved information and files, preparing quote packages, and presenting her work to the team through Teams and an authenticated dashboard. The existing workflow would stay in place, and Ava would only use systems IT approves. Any customer-facing message would be reviewed and approved by Lea & Braze before it is sent.

I'm working out the simplest way to connect Ava with Lea & Braze's email, Teams, files, and any existing Azure setup without changing the current workflow. Could you help me with the questions below?

Short answers are fine, and `not sure` is completely okay. If you already have a diagram, screenshot, policy, or system list that answers something, feel free to send that instead.

## Email and Teams

1. Where is the project quote inquiry mailbox actually hosted: Exchange Online, an Exchange Server at Lea & Braze, or another email provider? If it is not in Exchange Online, which product, version, and build is it using? Is the setup hybrid?
2. Which inbox or email address receives the quote requests? Is it a regular mailbox, shared mailbox, or distribution group?
3. Would it be okay to copy all project inquiries to a separate test mailbox while normal delivery continues unchanged? Later, could IT create a company-controlled Ava mailbox for sending and replies? Would that need a license or much setup time?

My starting suggestion depends on where the mailbox is hosted:

| Email setup | Suggested connection and sign-in |
| --- | --- |
| Exchange Online | Use Microsoft Graph through a dedicated Entra application whose access is limited to the approved Ava mailbox. |
| On-premises Exchange | Prefer an Exchange mail-flow rule that copies all project inquiries to an Exchange Online POC mailbox, then use Graph. If no cloud mailbox is available, use Exchange Web Services (EWS) over HTTPS with a dedicated non-personal identity and an authentication method approved by IT. SMTP relay would only handle outbound mail. |
| Hybrid Exchange | Use Graph for mailboxes in Exchange Online. For on-premises mailboxes, copy all project inquiries to the cloud POC mailbox or use EWS. The sign-in method follows the location of the mailbox. |
| Another hosted provider | Use the provider's API and OAuth if available. Otherwise, use IMAP for mailbox reading and SMTP for sending with dedicated service credentials. |

4. Does the suggestion for Lea & Braze's setup work with the current configuration and security rules? If not, which connection and sign-in method would you prefer?
5. Is there anything else in the email setup I should plan around, such as forwarding blocks, attachment limits, signatures, disclaimers, outside-email rules, spam protection, journaling, or retention?
6. Is Teams in the same Microsoft 365 tenant? Could I set Ava up for a small POC group in a private Team or channel? What admin or licensing steps would that take?

## Files

7. Where do the old inquiries, quotes, templates, pricing references, and similar project files live today? Are they on an SMB share, DFS, a NAS, SharePoint, OneDrive, Azure Files, or somewhere else?
8. If they are on SMB, DFS, or a NAS, can you share the paths, server type and version, and the Active Directory domain people use to access them?
9. How do engineers currently access shared files when working remotely or in the field? Do they use VPN, VDI, remote desktop, DFS or SMB paths, SharePoint/OneDrive sync, or another method?
10. Could IT make a small folder containing only the approved POC files, give Ava read-only access, and provide a separate place for Ava's output?
11. What kinds of files and file sizes should I expect, and roughly how much data is there? Are malware scanning, retention, backups, or a file-sync tool already in place?

## Azure and network

I will handle Ava's Azure architecture and technical requirements, including the Azure services or VMs, operating system, admin access, patching, endpoint protection, and security scanning. The Azure subscription and ownership arrangement are still to be decided.

12. Is the office already connected to Azure through a Site-to-Site VPN or ExpressRoute? If so, what can Azure currently reach, including private DNS or Active Directory?
13. What network rules should I know about between Lea & Braze and Azure? This could include outbound HTTPS, proxies, firewall allowlists, static IP addresses, DNS, certificates, or limits on inbound access.

## Accounts, data, and support

14. Are on-premises Active Directory and Entra ID connected? How do you normally set up application or service accounts, tenant approval, certificates, secrets, password rotation, MFA, and Conditional Access?
15. Are there any types of customer, project, pricing, employee, or old quote data that should not be moved into Azure or sent to an external AI service? Are there rules about where the data can be stored, masking it, how long I can keep it, or when I should delete it?
16. Does Lea & Braze need to receive any POC audit logs or security alerts? Who should I contact if there is a security issue or company access needs to be shut off quickly?
17. Are there any Lea & Braze-side licenses, reviews, approvals, or known blockers that could take extra time or cost money?
