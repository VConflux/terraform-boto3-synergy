resource "aws_instance" "MyInstance" {
    ami = var.ami_id
    instance_type = var.instance_type
    key_name = var.key_name

    subnet_id = aws_subnet.subnet1.id

    vpc_security_group_ids = [aws_security_group.my_security_group.id]

    tags = {
        Name = var.instance_name
    }   

}
