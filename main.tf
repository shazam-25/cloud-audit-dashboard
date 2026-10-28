terraform {
  required_providers {
    neon = {
      source  = "kislerdm/neon"
      version = "~> 0.18.0"
    }
  }
}

provider "neon" {}

resource "neon_project" "src_finops_db" {
  name      = "leveraging-cloud-services"
  region_id = "aws-us-east-2"
  org_id = "org-withered-hat-20534142"
  history_retention_seconds     = 21600
}

output "database_host" {
  value = neon_project.src_finops_db.database_host
}

output "connection_uri" {
  value     = neon_project.src_finops_db.connection_uri
  sensitive = true
}