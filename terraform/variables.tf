
variable "aws_region" {
  description = "AWS region for the project"
  type        = string
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 instance size"
  type        = string
  default     = "t3.micro"
}

variable "my_ip_cidr" {
  description = "Your public IPv4 address followed by /32"
  type        = string
}
