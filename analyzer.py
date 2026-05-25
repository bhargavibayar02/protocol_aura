def analyze_protocol(protocol):

    data = {

# ================= LAYER 7 =================
"HTTP": {
"layer": "Application Layer (Layer 7)",

"syntax": """
HTTP Request Format:
GET /index.html HTTP/1.1
Host: www.example.com

HTTP Response Format:
HTTP/1.1 200 OK
Content-Type: text/html
""",

"semantics": """
HTTP (HyperText Transfer Protocol) is a stateless, application-layer protocol used for communication between web clients and servers.

It follows a request-response model:
- Client sends request (GET, POST, PUT, DELETE)
- Server processes and responds

Key Characteristics:
- Stateless (each request independent)
- Text-based protocol
- Works over TCP

Used extensively in:
- Web browsing
- APIs
- REST services
""",

"timing": """
HTTP relies on TCP for reliable delivery.

Timing includes:
- TCP connection setup (3-way handshake)
- Request transmission
- Server processing delay
- Response delivery

Performance factors:
- Latency
- Server load
- Network congestion
""",

"attack": """
Common Attacks:
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- HTTP Flood (DoS)

These attacks exploit input validation and session management weaknesses.
""",

"mitigation": """
Mitigation Techniques:
- Use HTTPS (TLS encryption)
- Input validation & sanitization
- Content Security Policy (CSP)
- Secure cookies
""",

"quiz": [
{"q":"HTTP is which type of protocol?","options":["Stateful","Stateless","Encrypted","Binary"],"answer":"Stateless"},
{"q":"HTTP works on which layer?","options":["Transport","Application","Network","Data Link"],"answer":"Application"},
{"q":"Which method retrieves data?","options":["GET","POST","PUT","DELETE"],"answer":"GET"}
]
},
"DNS": {
            "layer": "Application Layer (Layer 7)",
            "syntax": """
DNS Query Format:
- Query: example.com Type:A
- Response: example.com IN A 93.184.216.34
""",
            "semantics": """
DNS (Domain Name System) translates human-readable domain names to IP addresses.

Key operations:
- Recursive queries (resolve domain using multiple servers)
- Iterative queries
- Caching for faster resolution

Used in:
- Web browsing
- Email delivery
- Network services
""",
            "timing": """
DNS Resolution Timing:
- Local resolver cache lookup
- Recursive or iterative query to authoritative server
- Response returned to client

Performance factors:
- Cache hits/misses
- Network latency
- Authoritative server response time
""",
            "attack": """
Common Attacks:
- DNS spoofing / cache poisoning
- DNS amplification (DDoS)
- NXDOMAIN attacks

Exploits weaknesses in query validation or server configuration.
""",
            "mitigation": """
Mitigation Techniques:
- Enable DNSSEC for authentication
- Monitor unusual traffic patterns
- Secure caching policies
- Rate-limiting for queries
""",
            "quiz": [
                {"q":"DNS resolves?","options":["MAC addresses","IP addresses","Ports","Packets"],"answer":"IP addresses"},
                {"q":"DNS default port?","options":[53,80,443,21],"answer":53},
                {"q":"Type A record returns?","options":["IPv4","IPv6","MAC","Domain"],"answer":"IPv4"}
            ]
        },


# ================= LAYER 6 =================
"TLS": {
"layer": "Presentation Layer (Layer 6)",

"syntax": """
TLS Handshake:
ClientHello → ServerHello → Certificate → Key Exchange → Secure Channel Established
""",

"semantics": """
TLS (Transport Layer Security) provides encryption, authentication, and integrity.

It ensures:
- Confidentiality (data encrypted)
- Integrity (no tampering)
- Authentication (server identity verified)

Used in:
- HTTPS
- Secure email
- VPNs
""",

"timing": """
TLS introduces additional delay due to handshake.

Phases:
1. Handshake (key exchange)
2. Session encryption
3. Data transmission

Modern TLS (1.3) reduces handshake latency.
""",

"attack": """
Attacks:
- SSL stripping
- Man-in-the-middle (MITM)
- Certificate spoofing
""",

"mitigation": """
Mitigation:
- Use TLS 1.3
- Enable HSTS
- Certificate validation
""",

"quiz":[
{"q":"TLS provides?","options":["Routing","Encryption","MAC","Session"],"answer":"Encryption"},
{"q":"Used in HTTPS?","options":["Yes","No","Sometimes","Rarely"],"answer":"Yes"},
{"q":"Layer?","options":["Presentation","Session","Transport","Physical"],"answer":"Presentation"}
]
},

# ================= LAYER 5 =================
"RPC": {
"layer": "Session Layer (Layer 5)",

"syntax": "Remote Procedure Call (function call over network)",

"semantics": """
RPC allows programs to execute functions on remote systems as if they were local.

It manages:
- Session establishment
- Synchronization
- Communication endpoints
""",

"timing": """
Includes:
- Request transmission
- Remote execution
- Response return

Latency depends on network delay and server processing.
""",

"attack": """
Attacks:
- Session hijacking
- Replay attacks
""",

"mitigation": """
Mitigation:
- Authentication tokens
- Session encryption
""",

"quiz":[
{"q":"RPC means?","options":["Remote Procedure Call","Random Packet Control","Routing Call","None"],"answer":"Remote Procedure Call"},
{"q":"Used for?","options":["Remote execution","Routing","Encryption","MAC"],"answer":"Remote execution"},
{"q":"Layer?","options":["Session","Application","Network","Physical"],"answer":"Session"}
]
},

# ================= LAYER 4 =================
"TCP": {
"layer": "Transport Layer (Layer 4)",

"syntax": """
TCP Header Fields:
- Source Port
- Destination Port
- Sequence Number
- Acknowledgment Number
- Flags (SYN, ACK, FIN)
""",

"semantics": """
TCP is a connection-oriented protocol that ensures reliable data delivery.

Features:
- Error detection
- Retransmission
- Flow control
- Congestion control
""",

"timing": """
3-way handshake:
SYN → SYN-ACK → ACK

Also includes:
- RTT measurement
- Congestion control algorithms
""",

"attack": """
Attacks:
- SYN Flood
- TCP Reset attack
""",

"mitigation": """
Mitigation:
- SYN cookies
- Firewall filtering
""",

"quiz":[
{"q":"TCP is?","options":["Connectionless","Connection-oriented","Stateless","Fast"],"answer":"Connection-oriented"},
{"q":"Handshake steps?","options":["2","3","4","5"],"answer":"3"},
{"q":"Ensures?","options":["Speed","Reliability","Routing","Encryption"],"answer":"Reliability"}
]
},
"UDP": {
    "layer": "Transport Layer (Layer 4)",

    "syntax": """
UDP Header Fields:
- Source Port
- Destination Port
- Length
- Checksum
""",

    "semantics": """
UDP (User Datagram Protocol) is a connectionless, lightweight transport protocol.

Key characteristics:
- Connectionless (no handshake)
- Minimal overhead
- No guarantee of delivery, ordering, or error correction
- Suitable for real-time applications where speed matters

Common uses:
- DNS queries
- VoIP (Voice over IP)
- Streaming media
- Online gaming
""",

    "timing": """
UDP timing is simple:
- Packet is sent without establishing a connection
- Receiver may acknowledge at application layer (optional)
- Low latency since no handshake or retransmission

Performance factors:
- Network congestion can cause packet loss
- Minimal delay, suitable for real-time traffic
""",

    "attack": """
Common attacks on UDP:
- UDP Flood (DoS)
- Amplification attacks (e.g., DNS amplification)
- Reflection attacks

Exploits UDP’s statelessness to overwhelm targets.
""",

    "mitigation": """
Mitigation techniques:
- Rate limiting and traffic shaping
- Firewall and ACL rules
- Disable unused UDP services
- Monitoring for abnormal traffic patterns
""",

    "quiz": [
        {"q":"UDP is connection-oriented or connectionless?","options":["Connection-oriented","Connectionless","Stateless","Reliable"],"answer":"Connectionless"},
        {"q":"UDP guarantees delivery?","options":["Yes","No","Partial","Sometimes"],"answer":"No"},
        {"q":"Common UDP applications?","options":["VoIP, DNS, Streaming","HTTP, FTP","SSH, Telnet","SMTP, POP3"],"answer":"VoIP, DNS, Streaming"}
    ]
},

# ================= LAYER 3 =================
"IP": {
"layer": "Network Layer (Layer 3)",

"syntax": "IP Header (Source IP, Destination IP, TTL)",

"semantics": """
IP handles logical addressing and routing of packets across networks.

It ensures packets reach destination using routing tables.
""",

"timing": """
Best-effort delivery:
- No guarantee of delivery
- No retransmission

Depends on routing efficiency.
""",

"attack": """
Attacks:
- IP spoofing
- ICMP flood
""",

"mitigation": """
Mitigation:
- Packet filtering
- Firewalls
""",

"quiz":[
{"q":"IP used for?","options":["Routing","Encryption","Session","MAC"],"answer":"Routing"},
{"q":"Delivery type?","options":["Guaranteed","Best effort","Reliable","Ordered"],"answer":"Best effort"},
{"q":"Layer?","options":["Network","Transport","Data","Physical"],"answer":"Network"}
]
},

# ================= LAYER 2 =================
"ETHERNET": {
"layer": "Data Link Layer (Layer 2)",

"syntax": "Frame: MAC Source → MAC Destination",

"semantics": """
Ethernet provides communication within a local network using MAC addresses.

It handles:
- Framing
- Error detection
""",

"timing": """
Frame transmission:
- CSMA/CD mechanism
- Collision detection
""",

"attack": """
Attacks:
- ARP spoofing
- MAC flooding
""",

"mitigation": """
Mitigation:
- Port security
- ARP inspection
""",

"quiz":[
{"q":"Uses?","options":["MAC","IP","DNS","Port"],"answer":"MAC"},
{"q":"Layer?","options":["Data Link","Network","Transport","Application"],"answer":"Data Link"},
{"q":"Attack?","options":["ARP spoof","XSS","SQL","None"],"answer":"ARP spoof"}
]
},

# ================= LAYER 1 =================
"FIBER": {
"layer": "Physical Layer (Layer 1)",

"syntax": "Binary data → Light pulses",

"semantics": """
Physical layer transmits raw bits through physical medium.

Fiber optics uses light signals for high-speed transmission.
""",

"timing": """
Continuous transmission with minimal delay.

Depends on:
- Medium quality
- Distance
""",

"attack": """
Attacks:
- Cable tapping
- Signal interception
""",

"mitigation": """
Mitigation:
- Physical security
- Encrypted transmission
""",

"quiz":[
{"q":"Transmits?","options":["Bits","Packets","Frames","Messages"],"answer":"Bits"},
{"q":"Medium?","options":["Light","Sound","Electric","Wireless"],"answer":"Light"},
{"q":"Layer?","options":["Physical","Network","Transport","Application"],"answer":"Physical"}
]
}

    }

    return {"data": data.get(protocol.upper(), None)}