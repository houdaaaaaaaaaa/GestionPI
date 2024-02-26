from django.db import models

class OrdinateurDeBureau(models.Model):
      pass

class UC(OrdinateurDeBureau):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    processeur = models.CharField(max_length=100)
    memoire_ram = models.CharField(max_length=100)
    capacite_stockage = models.CharField(max_length=100)
    carte_graphique = models.CharField(max_length=100)
    systeme_exploitation = models.CharField(max_length=100)
    ports_disponibles = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Moniteur(OrdinateurDeBureau):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    taille_ecran = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    type_panneau = models.CharField(max_length=100)
    connectivite = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Clavier(OrdinateurDeBureau):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    type_connexion = models.CharField(max_length=100)
    technologie = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Souris(OrdinateurDeBureau):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    type_connexion = models.CharField(max_length=100)
    technologie = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class HautParleur(OrdinateurDeBureau):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    configuration_audio = models.CharField(max_length=100)
    puissance_sortie = models.CharField(max_length=100)
    connectivite = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class OrdinateurPortable(models.Model):
     pass

class Ordinateur(OrdinateurPortable):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    processeur = models.CharField(max_length=100)
    memoire_ram = models.CharField(max_length=100)
    capacite_stockage = models.CharField(max_length=100)
    carte_graphique = models.CharField(max_length=100)
    systeme_exploitation = models.CharField(max_length=100)
    taille_ecran = models.CharField(max_length=100)
    autonomie_batterie = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Chargeur(OrdinateurPortable):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    compatibilite = models.CharField(max_length=100)
    puissance_sortie = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
    
class Serveurs(models.Model):
      pass
    
class Serveur(Serveurs):
    type = models.CharField(max_length=100)  # Rackable ou en tour
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    processeur = models.CharField(max_length=100)
    memoire_ram = models.CharField(max_length=100)
    capacite_stockage = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class BaieStockage(Serveurs):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class DisqueDurSSD(Serveurs):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    interface = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class MemoireRAMServeur(Serveurs):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class ProcesseurServeur(Serveurs):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    nombre_coeurs = models.IntegerField()
    frequence = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
    
class Réseau(models.Model):
    pass

class Routeur(Réseau):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    ports = models.IntegerField()
    vitesse = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Commutateur(Réseau):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    ports = models.IntegerField()
    type = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class PareFeu(Réseau):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    nombre_interfaces = models.IntegerField()
    type = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class PointAccesSansFil(Réseau):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    standard_wifi = models.CharField(max_length=100)
    nombre_antennes = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
    
class PériphériquesDeStockage(models.Model):
    pass

class DisqueDurExterne(PériphériquesDeStockage):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    interface = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class CleUSB(PériphériquesDeStockage):
    marque = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    interface = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class CarteMemoire(PériphériquesDeStockage):
    marque = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class LecteurDisqueOptique(PériphériquesDeStockage):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    type_disque = models.CharField(max_length=100)  # DVD, Blu-ray, etc.
    interface = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
    
class ImprimantesEtScanners(models.Model):
    pass

class Imprimante(ImprimantesEtScanners):
    TYPE_CHOICES = [
        ('Laser', 'Laser'),
        ('À jet d\'encre', 'À jet d\'encre')
    ]
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    fonctionnalites = models.TextField()
    vitesse_impression = models.CharField(max_length=100)
    resolution_impression = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Scanner(ImprimantesEtScanners):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    type_capteur = models.CharField(max_length=100)
    resolution_optique = models.CharField(max_length=100)
    vitesse_scan = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
    
class EquipementDeSauvegardeEtDeSecurite(models.Model):
    pass

class SauvegardeSurBande(EquipementDeSauvegardeEtDeSecurite):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    vitesse = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class SauvegardeSurDisque(EquipementDeSauvegardeEtDeSecurite):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    type_connexion = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class AlimentationSansInterruption(EquipementDeSauvegardeEtDeSecurite):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    puissance = models.CharField(max_length=100)
    autonomie = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class SurveillanceReseauSecurite(EquipementDeSauvegardeEtDeSecurite):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    type_surveillance = models.CharField(max_length=100)
    fonctionnalites = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
    
class Accessoires(models.Model):
    pass

class CableEthernet(Accessoires):
    longueur = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Catégorie (par exemple Cat5e, Cat6)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class CableUSB(Accessoires):
    longueur = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Type (par exemple USB-A vers USB-B)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Adaptateur(Accessoires):
    type_entree = models.CharField(max_length=100)
    type_sortie = models.CharField(max_length=100)
    fonctionnalites = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Connecteur(Accessoires):
    type = models.CharField(max_length=100)  # Type (par exemple HDMI, VGA)
    fonctionnalites = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
    
class AccessoiresDePresentation(models.Model):
    pass

class Projecteur(AccessoiresDePresentation):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    luminosite = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Type de projecteur (par exemple DLP, LCD)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class EcranInteractif(AccessoiresDePresentation):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    taille = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    fonctionnalites = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
    
class MaterielAudiovisuel(models.Model):
    pass

class CameraVideosurveillance(MaterielAudiovisuel):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    vision_nuit = models.BooleanField(default=False)
    angle_vue = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class SystemeConferenceAudiovisuelle(MaterielAudiovisuel):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    resolution_ecran = models.CharField(max_length=100)
    nombre_micros = models.IntegerField()
    capacite_salles = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
    
class Mobilite(models.Model):
    pass

class Tablette(Mobilite):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    taille_ecran = models.CharField(max_length=100)
    systeme_exploitation = models.CharField(max_length=100)
    capacite_stockage = models.CharField(max_length=100)
    memoire_ram = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class SmartphoneEntreprise(Mobilite):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    systeme_exploitation = models.CharField(max_length=100)
    capacite_stockage = models.CharField(max_length=100)
    memoire_ram = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class AccessoireMobile(Mobilite):
    type = models.CharField(max_length=100)  # Par exemple étui, chargeur, etc.
    marque = models.CharField(max_length=100)
    compatible_modele = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
    
class SystemesDeRefroidissement(models.Model):
    pass

class VentilateurBoitier(SystemesDeRefroidissement):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    taille = models.CharField(max_length=100)
    type_connexion = models.CharField(max_length=100)
    niveau_bruit = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class SystemeRefroidissementLiquide(SystemesDeRefroidissement):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Type de système (par exemple AIO, custom loop)
    capacite_refroidissement = models.CharField(max_length=100)
    niveau_bruit = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
    
class Logiciel(models.Model):
    pass

class SystemeExploitation(Logiciel):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Desktop, Server
    version = models.CharField(max_length=100)
    licence = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class LogicielProductivite(Logiciel):
    nom = models.CharField(max_length=100)
    suite = models.CharField(max_length=100)  # Microsoft Office, Google Workspace
    version = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class LogicielCRM(Logiciel):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Salesforce, Microsoft Dynamics 365
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class LogicielCollaboration(Logiciel):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Microsoft Project, Slack, Microsoft Teams
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class SolutionSauvegarde(Logiciel):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Veeam Backup & Replication, Commvault
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class LogicielSecurite(Logiciel):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Antivirus/antimalware, Pare-feu (Firewall)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class LogicielComptaFinance(Logiciel):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # QuickBooks, SAP
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class SolutionITSM(Logiciel):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # ServiceNow, Jira Service Management
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
    
    