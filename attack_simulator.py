def get_attack_data(layer):

    attacks = {

# ================= APPLICATION LAYER =================
"Application": [
{
"name": "Cross-Site Scripting (XSS)",
"flow": [
"Attacker injects malicious JavaScript into web input field",
"Server stores or reflects the script",
"Victim loads webpage",
"Script executes in victim browser",
"Session cookies stolen"
],
"impact": "Session hijacking, account takeover",
"detection": "Check unusual script execution, CSP violations",
"mitigation": "Input sanitization, Content Security Policy (CSP)"
},

{
"name": "SQL Injection",
"flow": [
"User input not validated",
"Attacker injects SQL query",
"Database executes malicious query",
"Sensitive data leaked"
],
"impact": "Database breach, data loss",
"detection": "Unexpected DB queries, logs",
"mitigation": "Prepared statements, ORM, input validation"
}
],

# ================= TRANSPORT =================
"Transport": [
{
"name": "SYN Flood Attack",
"flow": [
"Attacker sends大量 SYN packets",
"Server allocates resources for each request",
"No ACK received",
"Server resources exhausted"
],
"impact": "Denial of Service",
"detection": "Half-open connections spike",
"mitigation": "SYN cookies, rate limiting"
},

{
"name": "TCP Reset Attack",
"flow": [
"Attacker spoofs TCP RST packet",
"Injects into active session",
"Connection terminated abruptly"
],
"impact": "Session disruption",
"detection": "Unexpected RST packets",
"mitigation": "Packet filtering, sequence validation"
}
],

# ================= NETWORK =================
"Network": [
{
"name": "IP Spoofing",
"flow": [
"Attacker modifies source IP",
"Packets appear from trusted source",
"Bypasses filtering"
],
"impact": "Unauthorized access",
"detection": "Ingress filtering logs",
"mitigation": "IP validation, firewalls"
},

{
"name": "ICMP Flood",
"flow": [
"Attacker sends大量 ICMP echo requests",
"Target overwhelmed processing responses"
],
"impact": "Network congestion, DoS",
"detection": "ICMP spike",
"mitigation": "Rate limiting ICMP"
}
],

# ================= DATA LINK =================
"Data Link": [
{
"name": "ARP Spoofing",
"flow": [
"Attacker sends fake ARP replies",
"Associates own MAC with victim IP",
"Traffic redirected to attacker"
],
"impact": "Man-in-the-middle attack",
"detection": "Duplicate MAC entries",
"mitigation": "Dynamic ARP inspection"
},

{
"name": "MAC Flooding",
"flow": [
"Attacker floods switch with fake MACs",
"Switch CAM table overflows",
"Switch broadcasts all traffic"
],
"impact": "Sniffing possible",
"detection": "MAC table overflow",
"mitigation": "Port security"
}
],

# ================= PHYSICAL =================
"Physical": [
{
"name": "Cable Tapping",
"flow": [
"Attacker physically taps cable",
"Signal intercepted",
"Data captured"
],
"impact": "Data theft",
"detection": "Signal degradation",
"mitigation": "Secure infrastructure"
},

{
"name": "Jamming Attack",
"flow": [
"Attacker emits noise signals",
"Disrupts communication channel"
],
"impact": "Signal loss",
"detection": "Noise spike",
"mitigation": "Shielding, frequency hopping"
}
]

    }

    return attacks.get(layer, [])