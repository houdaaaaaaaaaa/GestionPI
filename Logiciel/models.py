from django.db import models

class SystemeExploitation(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Desktop, Server
    version = models.CharField(max_length=100)
    licence = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class LogicielProductivite(models.Model):
    nom = models.CharField(max_length=100)
    suite = models.CharField(max_length=100)  # Microsoft Office, Google Workspace
    version = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class LogicielCRM(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Salesforce, Microsoft Dynamics 365
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class LogicielCollaboration(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Microsoft Project, Slack, Microsoft Teams
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class SolutionSauvegarde(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Veeam Backup & Replication, Commvault
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class LogicielSecurite(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Antivirus/antimalware, Pare-feu (Firewall)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class LogicielComptaFinance(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # QuickBooks, SAP
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class SolutionITSM(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # ServiceNow, Jira Service Management
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
    
    
