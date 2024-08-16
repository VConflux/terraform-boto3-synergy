resource "tls_private_key" "key_tf" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

resource "aws_key_pair" "my_tf_key" {
  key_name   = var.key_name
  public_key = tls_private_key.key_tf.public_key_openssh
}

resource "local_file" "my_tf_key_pair" {
  content  = tls_private_key.key_tf.private_key_pem
  filename = var.my_tf_key_pair
}

output "public_key_content" {
  value     = tls_private_key.key_tf.public_key_openssh
  sensitive = true
}
