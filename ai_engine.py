def explain(protocol, data, question=None):

    # ================= SAFETY CHECK =================
    if not data:
        return "No data available for this protocol."

    # ================= BASE DETAILED EXPLANATION =================
    full_explanation = f"""
==============================
PROTOCOL: {protocol}
LAYER: {data['layer']}
==============================

1. OVERVIEW:
{data['semantics']}

This protocol plays a crucial role in the OSI model by enabling communication between systems in a structured and standardized way. It ensures interoperability between devices across different vendors and platforms.

--------------------------------------------------

2. SYNTAX (STRUCTURE):
{data['syntax']}

Syntax defines the format of messages exchanged between systems. It ensures that both sender and receiver interpret the data correctly.

--------------------------------------------------

3. SEMANTICS (MEANING):
Semantics refers to the meaning of each field in the protocol. It defines:
- What each message represents
- How systems should react
- Error handling mechanisms

--------------------------------------------------

4. TIMING & PERFORMANCE:
{data['timing']}

Timing is critical in networking systems and affects:
- Latency (delay in communication)
- Throughput (data transfer rate)
- Congestion control

Efficient timing ensures optimal network performance.

--------------------------------------------------

5. ATTACK ANALYSIS:
{data['attack']}

These attacks exploit weaknesses such as:
- Improper validation
- Lack of authentication
- Protocol design limitations

Attackers use these vulnerabilities to disrupt or gain unauthorized access.

--------------------------------------------------

6. MITIGATION STRATEGIES:
{data['mitigation']}

Security can be improved using:
- Encryption techniques
- Secure configurations
- Firewalls and filtering
- Regular monitoring and logging

--------------------------------------------------

7. REAL-WORLD APPLICATIONS:
This protocol is widely used in:
- Web systems
- Enterprise networks
- Cloud computing
- Distributed systems

--------------------------------------------------

8. ENGINEERING INSIGHT:
When designing systems using this protocol, engineers must consider:
- Scalability
- Fault tolerance
- Security
- Performance optimization

--------------------------------------------------
"""

    # ================= QUESTION-BASED RESPONSE =================
    if question:

        q = question.lower()

        # ===== ATTACK QUESTIONS =====
        if "attack" in q or "security" in q:
            return f"""
SECURITY ANALYSIS FOR {protocol}

Attack Types:
{data['attack']}

Impact:
These attacks can lead to data breaches, denial of service, or unauthorized access.

Mitigation:
{data['mitigation']}

Best Practice:
Always implement layered security (defense-in-depth).
"""

        # ===== TIMING QUESTIONS =====
        elif "timing" in q or "performance" in q:
            return f"""
⏱ TIMING & PERFORMANCE ANALYSIS

{data['timing']}

Key Factors:
- Latency
- Throughput
- Packet loss

Optimization Techniques:
- Load balancing
- Congestion control algorithms
"""

        # ===== WORKING QUESTIONS =====
        elif "working" in q or "how" in q:
            return f"""
WORKING OF {protocol}

{data['semantics']}

Step-by-step:
1. Data is formatted according to syntax
2. Transmitted across layers
3. Received and interpreted
4. Response generated (if applicable)

This ensures reliable communication between systems.
"""

        # ===== REAL-WORLD QUESTIONS =====
        elif "real" in q or "usage" in q:
            return f"""
REAL-WORLD USAGE

Used in:
- Internet communication
- Cloud services
- Enterprise systems

Example:
Web browsers use this protocol to communicate with servers.
"""

        # ===== DEFAULT FALLBACK =====
        else:
            return f"""
AI RESPONSE

Your Question: {question}

Based on the protocol:

{data['semantics']}

Additional Info:
{data['timing']}

Security:
{data['attack']} → {data['mitigation']}
"""

    # ================= DEFAULT RETURN =================
    return full_explanation