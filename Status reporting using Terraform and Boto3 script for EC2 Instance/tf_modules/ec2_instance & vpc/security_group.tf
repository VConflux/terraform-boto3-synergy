resource "aws_security_group" "my_security_group" {
    vpc_id = aws_vpc.my_vpc.id

    ingress {
        description = "Allow SSH from anywhere"
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]     # Allow access from any IP

    }
  
    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"     # -1 means all protocols
        cidr_blocks = ["0.0.0.0/0"]      # Allow outbound traffic to any IP
    }

    tags = {
      Name = "Allowing SSH"
    }
}