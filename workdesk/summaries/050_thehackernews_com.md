This article details a cybersecurity threat dubbed **"Prompt Poaching,"** where browser extensions are used to stealthily exfiltrate conversations from AI platforms like ChatGPT and DeepSeek.

Here is a summary of the key findings, the extensions involved, and the recommended actions.

### **The Malicious Extensions**
Two specific extensions, which collectively have over **900,000 users**, were found impersonating legitimate AI tools to steal data. They exfiltrate conversation content and every URL visited by the user to a remote server every 30 minutes.

1.  **Chat GPT for Chrome with GPT-5, Claude Sonnet & DeepSeek AI**
    *   **ID:** `fnmihdojmnkclgjpcoonokmkhjpjechg`
    *   **User Count:** 600,000+
2.  **AI Sidebar with Deepseek, ChatGPT, Claude, and more**
    *   **ID:** `inhcgfpbfdjbjogdfjbclgolkmhnooop`
    *   **User Count:** 300,000+

*Note: These extensions were designed to mimic a popular legitimate extension from "AITOPIA" to gain user trust.*

### **What is "Prompt Poaching"?**
Coined by researchers at **Secure Annex**, Prompt Poaching is the tactic of using browser extensions to capture sensitive AI chatbot interactions. 

**How it works:**
*   **Deceptive Consent:** The extensions ask for permission to collect "anonymous, non-identifiable analytics." 
*   **DOM Scraping:** Once installed, they look for specific elements within the web page (Document Object Model) to scrape the actual text of chat messages.
*   **Infrastructure Obfuscation:** Attackers use AI-powered web development platforms (like Lovable) to host privacy policies and C2 (Command and Control) servers to make their activities look like legitimate traffic.

### **"Legitimate" Extensions Joining the Trend**
The report highlights a concerning trend: established, popular extensions are also beginning to collect AI prompt data, often by updating their Terms of Service.
*   **Similarweb (1M+ users):** Updated its policy in early 2026 to explicitly state it collects prompts, queries, and uploaded files to analyze traffic metrics.
*   **Stayfocusd (600k users):** Also identified as engaging in prompt data collection.

These extensions may use more sophisticated methods, such as hijacking browser APIs (`fetch()` and `XMLHttpRequest`), to gather data from ChatGPT, Claude, Gemini, and Perplexity.

### **Risks to Users and Organizations**
The stolen data often contains highly sensitive information, including:
*   **Intellectual Property:** Proprietary code or business strategies pasted into AI tools.
*   **Corporate Espionage:** Exposure of internal URLs and confidential project names.
*   **Identity Theft:** Personal details shared during casual AI use.
*   **Phishing:** Data can be sold on underground forums to create highly targeted phishing campaigns.

### **Recommended Actions**
1.  **Immediate Removal:** Check your browser extensions (Chrome/Edge/Brave). If you have either of the two malicious IDs listed above, **remove them immediately.**
2.  **Audit Permissions:** Review the permissions of any "AI Sidebar" or "Chatbot Assistant" extensions. Be wary of those requesting access to "all websites" or "browsing history."
3.  **Check Privacy Policies:** For legitimate tools like Similarweb, review the latest privacy policy updates to see if they are now collecting your AI inputs.
4.  **Enterprise Policy:** Organizations should consider implementing policies that restrict the use of third-party AI extensions on company hardware to prevent "Shadow AI" data leaks.