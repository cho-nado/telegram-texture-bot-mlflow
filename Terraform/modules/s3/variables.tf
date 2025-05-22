variable "bucket_name" {
  description = "Bucket name"
  type        = string
}

variable "acl" {
  description = "ACL setting"
  type        = string
  default     = "private"
}