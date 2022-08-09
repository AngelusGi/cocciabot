## Variables

variable "resourcePrefix" {
  type        = string
  description = "Resource prefix name"
  default     = "TelegramBot"
}

variable "azureRegion" {
  type        = string
  default     = "westeurope"
  description = "Default Azure Region"
}


## Providers

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 2.67.0"
    }

    azurecaf = {
      source  = "aztfmod/azurecaf"
      version = "1.2.5"
    }
  }
}

provider "azurecaf" {
  features {}
}

provider "azurerm" {
  features {}
}


## Custom modules

module "tgBot" {
  source         = "./modules"
  resourcePrefix = var.resourcePrefix
  azureRegion    = var.azureRegion
}

