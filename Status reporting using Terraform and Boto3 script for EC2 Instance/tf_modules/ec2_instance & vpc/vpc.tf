resource "aws_vpc" "my_vpc" {
    cidr_block = var.vpc_cidr  
    tags = {
        Name = "my_vpc"
    } 
}


resource "aws_subnet" "subnet1" {
    vpc_id = aws_vpc.my_vpc.id
    cidr_block = var.public_subnet1
    map_public_ip_on_launch = true

    tags = {
        Name = "my_public_subnet1"
    }  
}


resource "aws_internet_gateway" "my_ig" {
    vpc_id = aws_vpc.my_vpc.id 

    tags = {
        Name = "my_igw"
    }  
}


resource "aws_route_table" "route_table_for_subnet1" {
    vpc_id = aws_vpc.my_vpc.id

    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.my_ig.id
    }

    tags = {
        Name = "public_subnet1_igw"
    }
  
}

resource "aws_route_table_association" "subnet1_route_table_association" {
    subnet_id = aws_subnet.subnet1.id
    route_table_id = aws_route_table.route_table_for_subnet1.id   
}