terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  credentials = file("lemon-project-credentials.json")

  project = "lemon-project-393220"
  region  = "us-central1"
  zone    = "us-central1-c"
}