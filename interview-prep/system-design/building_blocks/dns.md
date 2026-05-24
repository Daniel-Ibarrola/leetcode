# DNS (Domain Name System)

## What is it?
DNS translates human-readable domain names (`example.com`) into IP addresses (`93.184.216.34`) that computers use to route traffic. It's the internet's phone book — distributed, hierarchical, and cached at every layer.

## How a DNS lookup works (step by step)
1. You type `example.com` in your browser
2. Browser checks its local DNS cache → not found
3. OS checks its cache and `/etc/hosts` → not found
4. Query goes to your **recursive resolver** (usually your ISP or 8.8.8.8)
5. Resolver asks a **root nameserver** → "who handles `.com`?"
6. Root server returns the **TLD nameserver** for `.com`
7. Resolver asks the TLD nameserver → "who handles `example.com`?"
8. TLD returns the **authoritative nameserver** for `example.com`
9. Resolver asks the authoritative nameserver → returns the IP
10. Resolver caches the result and returns it to you

## Key record types
- **A** — maps a domain to an IPv4 address
- **AAAA** — maps a domain to an IPv6 address
- **CNAME** — alias; maps one domain to another domain (not an IP)
- **MX** — mail server for a domain
- **TXT** — arbitrary text; used for domain verification, SPF, DKIM
- **NS** — nameservers authoritative for a domain

## TTL (Time To Live)
- Every DNS record has a TTL (seconds) — how long resolvers/clients cache it
- Low TTL (60s) → changes propagate fast, but more DNS queries
- High TTL (86400s = 1 day) → faster resolution (cache hits), but changes are slow to propagate
- During incident response or migration, lower TTL before making changes

## DNS for system design

### Load balancing via DNS
- **Round-robin DNS** — return multiple IPs for the same domain; clients get a different one each time
- Simple, but clients cache the IP and stick to it until TTL expires

### GeoDNS / Anycast
- Return different IPs based on the client's location
- User in Europe gets a European server IP; user in Asia gets an Asian one
- Used by CDNs and global services to route users to the nearest datacenter

### Failover
- If primary IP goes down, update DNS to point to the backup
- Limited by TTL — propagation delay means some clients still hit the old IP

## Trade-offs

| Pro | Con |
|-----|-----|
| Massively distributed and cached — scales globally | Changes aren't instant (TTL-bound propagation delay) |
| Simple to configure routing/failover via record updates | DNS hijacking/spoofing is a real attack vector |
| GeoDNS enables easy geographic routing | Round-robin DNS is a poor substitute for a real load balancer |
| No single point of failure (multiple nameservers) | Clients ignore TTL and cache longer than they should |

## When DNS comes up in interviews
- **Global traffic routing** — "how do users in different regions hit the nearest datacenter?" → GeoDNS
- **Failover** — "how do you handle a datacenter going down?" → DNS failover (with low TTL)
- **Service discovery** — internal DNS (e.g., Kubernetes DNS) lets services find each other by name
- **CDN integration** — CDNs use CNAME records to intercept traffic before it hits your origin
