data "aws_region" "current" {}
data "aws_caller_identity" "current" {}
data "aws_kms_alias" "s3" {
  name = "alias/aws/s3"
}
data "aws_availability_zones" "az" {
  state = "available"
}