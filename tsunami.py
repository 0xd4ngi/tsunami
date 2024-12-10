from icmplib import ICMPv4Socket, ICMPRequest, ICMPReply, resolve # type: ignore
import socket

def send_icmp_request(hostname):
    # Resolve the hostname to an IPv4 address
    target_ip = resolve(hostname, socket.AF_INET)
    print(f"Resolved {hostname} to {target_ip}")

    # Create an ICMPv4 socket
    with ICMPv4Socket() as socket:
        # Create an ICMP Echo Request
        request = ICMPRequest(target_ip, sequence=1)

        # Send the ICMP request
        socket.send(request)

        print(f"Sent ICMP Echo Request to {target_ip}")

        # Wait for the reply
        reply = socket.receive(request, timeout=2)

        if isinstance(reply, ICMPReply):
            print(f"Received ICMP Echo Reply from {target_ip}")
            print(f"  Round-trip time: {reply.time} ms")
            print(f"  Sequence: {reply.sequence}")
        else:
            print("No reply received. The host may be unreachable or ICMP is blocked.")

# Example usage
if __name__ == "__main__":
    website = "bennett.edu.in"  # Replace with the desired website
    send_icmp_request(website)
