terraform {

  required_version = "~> 1.10.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.14.0"
    }
  }

  backend "azurerm" {
    use_azuread_auth = true
  }

}

provider "azurerm" {
  subscription_id = var.subscription
  features {
    key_vault {
      purge_soft_delete_on_destroy          = true
      purge_soft_deleted_keys_on_destroy    = true
      purge_soft_deleted_secrets_on_destroy = true
      recover_soft_deleted_key_vaults       = true
      recover_soft_deleted_keys             = true
      recover_soft_deleted_secrets          = true
    }
    subscription {
      prevent_cancellation_on_destroy = true
    }
  }
}

