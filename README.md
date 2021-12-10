# **Capstone Project of the Machine Learning ZoomCamp course**

## **Table of contents:**

- [About the project](#about-the-project)
- [Dataset](#dataset)
- [Data preparation and feature matrix](#data-preparation-and-feature-matrix)
- [Machine Learning Models](#machine-learning-models)
- [Python virtual environment and installation of required libraries](#python-virtual-environment-and-installation-of-required-libraries)
- [How to run this app as a web service in a local server?](#how-to-run-this-app-as-a-web-service-in-a-local-server)
- [How to run this app as a web service in the cloud?](#how-to-run-this-app-as-a-web-service-in-the-cloud)
- [Structure of the repository](#structure-of-the-repository)
- [Contact](#contact)

## **About the project**

[Antimicrobial peptides](https://en.wikipedia.org/wiki/Antimicrobial_peptides) (AMPs) are small bioactive drugs, commonly with fewer than 50 amino acids, which have appeared as promising compounds to control infectious disease caused by multi-drug resistant bacteria or superbugs. These superbugs are not treatable with the available drugs because of the development of some mechanisms to avoid the action of these compounds, which is known as antimicrobial resistance (AMR). According to the World Health Organization, AMR is one of the [top ten global public health threats facing humanity in this century](https://www.who.int/news-room/fact-sheets/detail/antimicrobial-resistance), so it is important to search for AMPs that combat these superbugs and prevent AMR.

However, the search for AMPs to combat superbugs by experimental methods is unfeasible because of the huge number of these compounds. So, it is required to explore other methods for handling this problem, and machine/deep learning models could be great candidates for this task. Thus, in this project I created some machine/deep learning binary classifiers to predict the activity of antimicrobial peptides.

## **Dataset**

The [dataset](https://biocom-ampdiscover.cicese.mx/dataset) for this project consists of text files (in FASTA format) with sequences of active and non-active AMPs. The active AMPs were obtained by experimental assays, while the non-active peptides were derived from computational methods. The following table summarizes the dataset partitions and the number of instances in each one.

|Dataset partition|Size|AMPs|non-AMPs|
|:-:|---|---|---|
|Training|19548|9781|9767|
|Test|5125|2564|2561|
|External|15685|4914|10771|

AMPs can have more than one activity, including antibacterial, antifungal, antiparasitic, antiviral, among others. Training and Test partitions have active AMPs with a single activity, while the external partition has AMPs with more than one activity and it represents a more real scenario of virtual screening with much more non active AMPs than the active ones.

## **Data preparation and feature matrix**

## **Machine Learning Models**

## **Python virtual environment and installation of required libraries**

## **How to run this app as a web service in a local server?**

## **How to run this app as a web service in the cloud?**

## **Structure of the repository**

## **Contact**

If you have comments or suggestions about this project, you can [open an issue](https://github.com/sayalaruano/MidtermProject-MLZoomCamp/issues/new) in this repository, or email me at sebasar1245@gamil.com.
