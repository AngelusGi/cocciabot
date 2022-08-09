## Resource Group

resource "azurerm_resource_group" "rg" {
  name     = local.rgp_shared_name
  location = var.az_region

  tags = var.default_tags
}

