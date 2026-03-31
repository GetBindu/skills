# Bindu Skills Registry

Welcome to the Bindu Skills Registry. This is where we keep a catalog of everything AI agents in the Bindu ecosystem can do — from searching scientific papers to designing proteins to analyzing clinical data.

## Understanding Skills: A Simple Explanation

Let's start with the basics. What exactly is a "skill" in Bindu?

### Skills Are Like Job Descriptions

Imagine you're hiring someone for a job. Before they start working, you write a job description that explains:
- What tasks they'll perform
- What information they need to do those tasks
- What results they should produce
- What tools or knowledge they need

That's exactly what a skill is. It's a **job description for AI agents**.

### What Skills Are NOT

Here's something important: skills are not the actual code that does the work. They're just the description of what needs to be done.

Think of it this way:
- A **recipe** tells you what ingredients you need and what steps to follow
- But the recipe itself doesn't cook the food — you do that

Similarly:
- A **skill definition** tells an agent what inputs it needs and what outputs to produce
- But the agent's own code does the actual work

### Why This Matters

This separation is powerful because:

1. **Anyone can understand what an agent does** — You don't need to read code. Just look at the skill definition.

2. **Different agents can implement the same skill differently** — One agent might search PubMed using Python, another might use a different approach. As long as they both follow the skill's contract (same inputs, same outputs), they both "have" that skill.

3. **Skills are reusable knowledge** — When someone creates a skill definition, every agent developer can use it as a blueprint.

## Who Should Use This Repository?

This repository serves two different groups of people:

### If You're Building an AI Agent

You're here to discover what capabilities you can give your agent. Think of this as a menu of superpowers.

When you find a skill you want your agent to have:
1. Read the skill's `README.md` to understand what it does
2. Look at the `skill.yaml` file to see the technical details (what inputs it expects, what outputs it produces)
3. Check the `examples/` folder to see how it works in practice
4. Implement that capability in your agent's code
5. When you register your agent, declare that it has this skill

### If You're a Researcher or User

You're here to understand what an AI agent can actually do.

When you see badges on an agent's profile (like "PubMed", "BLAST", "AlphaFold"), those are skills. Click on any skill to learn:
- What task it performs
- What information it needs from you
- What results it gives back
- How reliable it is

## How This Repository Is Organized

All skills live at the root level of the repository, each in its own folder. We've grouped them by category in this README to make it easier to find related capabilities.

Here's the structure:

```
skills/
├── pubmed/              # Each skill has its own folder
├── blast/
├── alphafold/
├── rdkit/
├── ...
└── _templates/          # Starter templates for creating new skills
```

Each skill folder contains:
- `skill.yaml` - The technical contract
- `README.md` - Human-readable documentation
- `examples/` - Usage examples (optional)
- `verify.py` - Capability proof script (optional)

## Available Skills

### Literature & Search
- [**adaptyv**](./adaptyv) — Adaptive literature search and synthesis
- [**arxiv**](./arxiv) — Search preprints from ArXiv across all categories
- [**arxiv-database**](./arxiv-database) — ArXiv database access
- [**autoresearch**](./autoresearch) — Automated research workflows
- [**bgpt-paper-search**](./bgpt-paper-search) — BioGPT-powered paper search
- [**biorxiv-database**](./biorxiv-database) — BioRxiv preprint database
- [**citation-management**](./citation-management) — Manage citations and references
- [**corpus-search**](./corpus-search) — Search across document corpora
- [**literature-deep-research**](./literature-deep-research) — Deep dive literature analysis
- [**literature-meta-search**](./literature-meta-search) — Meta-search across multiple sources
- [**literature-review**](./literature-review) — Systematic literature reviews
- [**openalex-database**](./openalex-database) — OpenAlex scholarly database
- [**osti-database**](./osti-database) — OSTI scientific database
- [**perplexity-search**](./perplexity-search) — Perplexity AI-powered search
- [**pubmed**](./pubmed) — Search NCBI PubMed for scientific articles
- [**pubmed-database**](./pubmed-database) — PubMed database access
- [**scholar-evaluation**](./scholar-evaluation) — Evaluate scholarly work
- [**scholar-search**](./scholar-search) — Google Scholar search
- [**semantic-scholar**](./semantic-scholar) — Semantic Scholar API access

### Sequences & Genomics
- [**blast**](./blast) — NCBI BLAST sequence alignment
- [**biopython**](./biopython) — Biological computation with BioPython
- [**ena-database**](./ena-database) — European Nucleotide Archive
- [**ensembl-database**](./ensembl-database) — Ensembl genome database
- [**gene-database**](./gene-database) — Gene information databases
- [**gene-enrichment**](./gene-enrichment) — Gene set enrichment analysis
- [**gget**](./gget) — Genomic data retrieval toolkit
- [**peptide-msa**](./peptide-msa) — Peptide multiple sequence alignment
- [**peptide-sequences**](./peptide-sequences) — Peptide sequence analysis
- [**sequence**](./sequence) — General sequence analysis
- [**sequence-retrieval**](./sequence-retrieval) — Retrieve biological sequences
- [**uniprot**](./uniprot) — UniProt protein database query
- [**uniprot-database**](./uniprot-database) — UniProt database access

### Protein Structures & Design
- [**alphafold**](./alphafold) — AlphaFold protein structure prediction
- [**alphafold-database**](./alphafold-database) — AlphaFold structure database
- [**boltz**](./boltz) — Boltz structure prediction
- [**boltzgen**](./boltzgen) — Boltz generative models
- [**chai**](./chai) — Chai protein design
- [**diffdock**](./diffdock) — DiffDock molecular docking
- [**esm**](./esm) — ESM protein language models
- [**foldseek**](./foldseek) — Fast protein structure search
- [**ligandmpnn**](./ligandmpnn) — LigandMPNN protein-ligand design
- [**pdb**](./pdb) — Protein Data Bank access
- [**pdb-database**](./pdb-database) — PDB database queries
- [**protein-design-workflow**](./protein-design-workflow) — End-to-end protein design
- [**protein-interactions**](./protein-interactions) — Protein-protein interactions
- [**protein-qc**](./protein-qc) — Protein quality control
- [**protein-structure-retrieval**](./protein-structure-retrieval) — Retrieve protein structures
- [**protein-therapeutic-design**](./protein-therapeutic-design) — Therapeutic protein design
- [**proteinmpnn**](./proteinmpnn) — ProteinMPNN design
- [**rfdiffusion**](./rfdiffusion) — RFdiffusion generative design
- [**solublempnn**](./solublempnn) — SoluBLEMPNN solubility optimization
- [**structure-contact-analysis**](./structure-contact-analysis) — Analyze protein contacts

### Drug Discovery & Chemistry
- [**askcos**](./askcos) — Computer-aided synthesis planning
- [**bindingdb-database**](./bindingdb-database) — BindingDB binding affinity data
- [**cas**](./cas) — CAS Registry chemical substances
- [**chembl**](./chembl) — ChEMBL bioactivity database
- [**chembl-database**](./chembl-database) — ChEMBL database access
- [**chemical-compound-retrieval**](./chemical-compound-retrieval) — Retrieve chemical compounds
- [**chemical-safety**](./chemical-safety) — Chemical safety information
- [**datamol**](./datamol) — Molecular data processing
- [**deepchem**](./deepchem) — Deep learning for chemistry
- [**drug-drug-interaction**](./drug-drug-interaction) — Drug interaction analysis
- [**drug-repurposing**](./drug-repurposing) — Drug repurposing strategies
- [**drug-research**](./drug-research) — Drug discovery research
- [**drug-target-validation**](./drug-target-validation) — Validate drug targets
- [**drugbank-database**](./drugbank-database) — DrugBank pharmaceutical database
- [**hmdb-database**](./hmdb-database) — Human Metabolome Database
- [**matchms**](./matchms) — Mass spectrometry data processing
- [**medchem**](./medchem) — Medicinal chemistry tools
- [**molfeat**](./molfeat) — Molecular featurization
- [**moltbook**](./moltbook) — Molecular notebook
- [**nistwebbook**](./nistwebbook) — NIST Chemistry WebBook
- [**pubchem**](./pubchem) — PubChem chemical database
- [**pubchem-database**](./pubchem-database) — PubChem database access
- [**pytdc**](./pytdc) — Therapeutics Data Commons
- [**rdkit**](./rdkit) — RDKit cheminformatics toolkit
- [**tdc**](./tdc) — Therapeutics Data Commons
- [**torchdrug**](./torchdrug) — PyTorch for drug discovery
- [**zinc-database**](./zinc-database) — ZINC compound database

### Clinical & Medical
- [**adverse-event-detection**](./adverse-event-detection) — Detect adverse drug events
- [**cancer-variant-interpretation**](./cancer-variant-interpretation) — Interpret cancer variants
- [**cbioportal-database**](./cbioportal-database) — cBioPortal cancer genomics
- [**clinical-decision-support**](./clinical-decision-support) — Clinical decision support systems
- [**clinical-guidelines**](./clinical-guidelines) — Medical guidelines and protocols
- [**clinical-reports**](./clinical-reports) — Generate clinical reports
- [**clinical-trial-design**](./clinical-trial-design) — Design clinical trials
- [**clinical-trial-matching**](./clinical-trial-matching) — Match patients to trials
- [**clinicaltrials-database**](./clinicaltrials-database) — ClinicalTrials.gov database
- [**clinpgx-database**](./clinpgx-database) — Clinical pharmacogenomics
- [**clinvar-database**](./clinvar-database) — ClinVar variant database
- [**cosmic-database**](./cosmic-database) — COSMIC cancer mutations
- [**depmap**](./depmap) — Cancer Dependency Map
- [**disease-research**](./disease-research) — Disease research tools
- [**fda-database**](./fda-database) — FDA regulatory database
- [**gnomad-database**](./gnomad-database) — gnomAD population genetics
- [**gwas-database**](./gwas-database) — GWAS catalog database
- [**gwas-drug-discovery**](./gwas-drug-discovery) — GWAS for drug discovery
- [**gwas-finemapping**](./gwas-finemapping) — GWAS fine-mapping
- [**gwas-snp-interpretation**](./gwas-snp-interpretation) — Interpret GWAS SNPs
- [**gwas-study-explorer**](./gwas-study-explorer) — Explore GWAS studies
- [**gwas-trait-to-gene**](./gwas-trait-to-gene) — Map traits to genes
- [**immunotherapy-response-prediction**](./immunotherapy-response-prediction) — Predict immunotherapy response
- [**infectious-disease**](./infectious-disease) — Infectious disease analysis
- [**pharmacovigilance**](./pharmacovigilance) — Drug safety monitoring
- [**precision-medicine-stratification**](./precision-medicine-stratification) — Stratify patients
- [**precision-oncology**](./precision-oncology) — Precision cancer medicine
- [**rare-disease-diagnosis**](./rare-disease-diagnosis) — Diagnose rare diseases
- [**treatment-plans**](./treatment-plans) — Generate treatment plans
- [**variant-analysis**](./variant-analysis) — Genetic variant analysis
- [**variant-interpretation**](./variant-interpretation) — Interpret genetic variants

### Omics & Systems Biology
- [**anndata**](./anndata) — Annotated data matrices
- [**arboreto**](./arboreto) — Gene regulatory network inference
- [**bioservices**](./bioservices) — Access biological web services
- [**cellxgene-census**](./cellxgene-census) — Single-cell data census
- [**cobrapy**](./cobrapy) — Constraint-based metabolic modeling
- [**crispr-screen-analysis**](./crispr-screen-analysis) — Analyze CRISPR screens
- [**epigenomics**](./epigenomics) — Epigenetic analysis
- [**expression-data-retrieval**](./expression-data-retrieval) — Retrieve gene expression data
- [**geo-database**](./geo-database) — GEO gene expression database
- [**gtex-database**](./gtex-database) — GTEx tissue expression
- [**immune-repertoire-analysis**](./immune-repertoire-analysis) — Immune repertoire sequencing
- [**interpro-database**](./interpro-database) — InterPro protein families
- [**jaspar-database**](./jaspar-database) — JASPAR transcription factor binding
- [**kegg-database**](./kegg-database) — KEGG pathway database
- [**lamindb**](./lamindb) — Data management for biology
- [**metabolism**](./metabolism) — Metabolic pathway analysis
- [**metabolomics**](./metabolomics) — Metabolomics workflows
- [**metabolomics-analysis**](./metabolomics-analysis) — Analyze metabolomics data
- [**metabolomics-workbench-database**](./metabolomics-workbench-database) — Metabolomics Workbench
- [**monarch-database**](./monarch-database) — Monarch disease-gene database
- [**multi-omics-integration**](./multi-omics-integration) — Integrate multi-omics data
- [**multiomic-disease-characterization**](./multiomic-disease-characterization) — Multi-omics disease profiling
- [**network-pharmacology**](./network-pharmacology) — Network-based pharmacology
- [**opentargets-database**](./opentargets-database) — Open Targets drug discovery
- [**proteomics-analysis**](./proteomics-analysis) — Proteomics data analysis
- [**pydeseq2**](./pydeseq2) — Differential expression analysis
- [**pyopenms**](./pyopenms) — Mass spectrometry analysis
- [**reactome-database**](./reactome-database) — Reactome pathway database
- [**rnaseq-deseq2**](./rnaseq-deseq2) — RNA-seq with DESeq2
- [**scanpy**](./scanpy) — Single-cell analysis in Python
- [**scvelo**](./scvelo) — RNA velocity analysis
- [**scvi-tools**](./scvi-tools) — Single-cell variational inference
- [**single-cell**](./single-cell) — Single-cell analysis
- [**spatial-omics-analysis**](./spatial-omics-analysis) — Spatial omics analysis
- [**spatial-transcriptomics**](./spatial-transcriptomics) — Spatial transcriptomics
- [**string-database**](./string-database) — STRING protein interactions
- [**systems-biology**](./systems-biology) — Systems biology modeling

### Lab Integration & Automation
- [**benchling-integration**](./benchling-integration) — Benchling LIMS integration
- [**cell-free-expression**](./cell-free-expression) — Cell-free protein expression
- [**dnanexus-integration**](./dnanexus-integration) — DNAnexus platform integration
- [**ginkgo-cloud-lab**](./ginkgo-cloud-lab) — Ginkgo Bioworks cloud lab
- [**labarchive-integration**](./labarchive-integration) — LabArchives ELN integration
- [**latchbio-integration**](./latchbio-integration) — Latch Bio platform integration
- [**omero-integration**](./omero-integration) — OMERO image data management
- [**opentrons-integration**](./opentrons-integration) — Opentrons liquid handling
- [**protocolsio-integration**](./protocolsio-integration) — Protocols.io integration
- [**pylabrobot**](./pylabrobot) — Lab automation with Python

### Data Analysis & Statistics
- [**dask**](./dask) — Parallel computing with Dask
- [**datavis**](./datavis) — Data visualization tools
- [**exploratory-data-analysis**](./exploratory-data-analysis) — EDA workflows
- [**polars**](./polars) — Fast DataFrame library
- [**pyhealth**](./pyhealth) — Healthcare data analysis
- [**scikit-learn**](./scikit-learn) — Machine learning in Python
- [**scikit-survival**](./scikit-survival) — Survival analysis
- [**shap**](./shap) — Model interpretability with SHAP
- [**statistical-analysis**](./statistical-analysis) — Statistical analysis tools
- [**statistical-modeling**](./statistical-modeling) — Statistical modeling
- [**statsmodels**](./statsmodels) — Statistical models in Python
- [**vaex**](./vaex) — Out-of-core DataFrames

### Visualization & Plotting
- [**datacommons-client**](./datacommons-client) — Google Data Commons
- [**geopandas**](./geopandas) — Geographic data analysis
- [**infographics**](./infographics) — Create infographics
- [**matplotlib**](./matplotlib) — Plotting with Matplotlib
- [**plotly**](./plotly) — Interactive plots with Plotly
- [**scientific-schematics**](./scientific-schematics) — Scientific diagrams
- [**scientific-slides**](./scientific-slides) — Create scientific presentations
- [**scientific-visualization**](./scientific-visualization) — Advanced scientific plots
- [**seaborn**](./seaborn) — Statistical data visualization

### Materials & Engineering
- [**ase**](./ase) — Atomic Simulation Environment
- [**fem-analysis**](./fem-analysis) — Finite element analysis
- [**geometry-generator**](./geometry-generator) — Generate geometric structures
- [**materials**](./materials) — Materials science tools
- [**mopac**](./mopac) — Molecular orbital calculations
- [**pymatgen**](./pymatgen) — Materials analysis with Python
- [**qmmm_adaptive**](./qmmm_adaptive) — QM/MM adaptive simulations

### Machine Learning & AI
- [**pytorch-lightning**](./pytorch-lightning) — PyTorch Lightning framework
- [**pufferlib**](./pufferlib) — Reinforcement learning library
- [**stable-baselines3**](./stable-baselines3) — RL algorithms
- [**torch_geometric**](./torch_geometric) — Graph neural networks
- [**transformers**](./transformers) — Hugging Face transformers
- [**umap-learn**](./umap-learn) — Dimensionality reduction

### Quantum & Physics
- [**cirq**](./cirq) — Google's quantum computing framework
- [**pennylane**](./pennylane) — Quantum machine learning
- [**qiskit**](./qiskit) — IBM quantum computing
- [**qutip**](./qutip) — Quantum toolbox in Python

### Scientific Writing & Communication
- [**diagramming**](./diagramming) — Create diagrams
- [**docx**](./docx) — Word document processing
- [**latex-posters**](./latex-posters) — LaTeX poster creation
- [**markdown-mermaid-writing**](./markdown-mermaid-writing) — Markdown with diagrams
- [**markitdown**](./markitdown) — Markdown conversion tools
- [**paper-2-web**](./paper-2-web) — Convert papers to web format
- [**pdf**](./pdf) — PDF processing
- [**peer-review**](./peer-review) — Peer review assistance
- [**pptx-posters**](./pptx-posters) — PowerPoint poster creation
- [**scientific-brainstorming**](./scientific-brainstorming) — Brainstorm research ideas
- [**scientific-critical-thinking**](./scientific-critical-thinking) — Critical analysis
- [**scientific-writing**](./scientific-writing) — Scientific writing assistance
- [**venue-templates**](./venue-templates) — Conference/journal templates
- [**write-review-paper**](./write-review-paper) — Write review papers
- [**xlsx**](./xlsx) — Excel spreadsheet processing

### Web & Data Collection
- [**browser-automation**](./browser-automation) — Automate web browsers
- [**firecrawl-scraper**](./firecrawl-scraper) — Web scraping with Firecrawl
- [**websearch**](./websearch) — General web search

### Business & Economics
- [**alpha-vantage**](./alpha-vantage) — Financial market data
- [**commodity-profile**](./commodity-profile) — Commodity market profiles
- [**comtrade-trade**](./comtrade-trade) — UN Comtrade trade data
- [**denario**](./denario) — Economic analysis
- [**edgartools**](./edgartools) — SEC EDGAR filings
- [**fred-economic-data**](./fred-economic-data) — Federal Reserve economic data
- [**hedgefundmonitor**](./hedgefundmonitor) — Hedge fund monitoring
- [**market-research-reports**](./market-research-reports) — Market research
- [**minerals-data**](./minerals-data) — Minerals market data
- [**minerals-gov-monitor**](./minerals-gov-monitor) — USGS minerals monitoring
- [**minerals-news-monitor**](./minerals-news-monitor) — Minerals news tracking
- [**minerals-viz**](./minerals-viz) — Minerals data visualization
- [**minerals-web-ingest**](./minerals-web-ingest) — Minerals web data ingestion
- [**research-grants**](./research-grants) — Research funding opportunities
- [**usfiscaldata**](./usfiscaldata) — US fiscal data

### Utilities & Infrastructure
- [**get-available-resources**](./get-available-resources) — Query available resources
- [**infinite**](./infinite) — Bindu Infinite platform integration
- [**modal**](./modal) — Modal serverless compute
- [**open-notebook**](./open-notebook) — Open notebook formats
- [**research-collect**](./research-collect) — Collect research data
- [**research-experiment**](./research-experiment) — Experiment tracking
- [**research-implement**](./research-implement) — Implementation workflows
- [**research-lookup**](./research-lookup) — Research database lookup
- [**research-pipeline**](./research-pipeline) — Research pipelines
- [**research-plan**](./research-plan) — Plan research projects
- [**research-review**](./research-review) — Review research
- [**research-subscription**](./research-subscription) — Subscribe to research updates
- [**research-survey**](./research-survey) — Research surveys
- [**tooluniverse**](./tooluniverse) — Tool discovery and management

### Creative & Specialized
- [**chord-analysis**](./chord-analysis) — Music chord analysis
- [**generate-image**](./generate-image) — Image generation
- [**image-analysis**](./image-analysis) — Analyze images
- [**lsystem-executor**](./lsystem-executor) — L-system fractal generation
- [**midi-generator**](./midi-generator) — Generate MIDI music
- [**music-corpus**](./music-corpus) — Music corpus analysis
- [**pointcloud-generator**](./pointcloud-generator) — Generate point clouds
- [**stl-renderer**](./stl-renderer) — Render 3D STL files

### Advanced Research Tools
- [**aeon**](./aeon) — Time series analysis
- [**antibody-engineering**](./antibody-engineering) — Antibody design
- [**binder-design**](./binder-design) — Protein binder design
- [**binder-discovery**](./binder-discovery) — Discover protein binders
- [**binding-characterization**](./binding-characterization) — Characterize binding
- [**candidate-ranking**](./candidate-ranking) — Rank candidates
- [**conservation-map**](./conservation-map) — Conservation analysis
- [**data-storytelling**](./data-storytelling) — Tell stories with data
- [**hypothesis-generation**](./hypothesis-generation) — Generate hypotheses
- [**idea-generation**](./idea-generation) — Generate research ideas
- [**investigation-plotter**](./investigation-plotter) — Plot investigations
- [**motif-clustering**](./motif-clustering) — Cluster sequence motifs
- [**motif-detection**](./motif-detection) — Detect sequence motifs
- [**mutation-generator**](./mutation-generator) — Generate mutations
- [**phylogenetics**](./phylogenetics) — Phylogenetic analysis
- [**polygenic-risk-score**](./polygenic-risk-score) — Calculate PRS
- [**prompt-engineering-patterns**](./prompt-engineering-patterns) — Prompt engineering
- [**structural-variant-analysis**](./structural-variant-analysis) — Analyze SVs
- [**target-research**](./target-research) — Research drug targets

## Contributing: Adding Your Own Skills

We welcome new skills! If you've identified a capability that agents should have, here's how to add it.

### Before You Start

Ask yourself:
1. **Is this a distinct capability?** — Does it do something different from existing skills?
2. **Is it reusable?** — Would multiple agents benefit from having this skill?
3. **Can you define clear inputs and outputs?** — Skills need well-defined contracts.

### The Process

**Step 1: Fork this repository**

Create your own copy so you can make changes.

**Step 2: Choose a descriptive name**

Pick a clear, lowercase name for your skill using hyphens for spaces. For example:
- `pubmed-search` or just `pubmed`
- `protein-structure-prediction`
- `clinical-trial-matching`

Look at existing skills to see the naming convention.

**Step 3: Create your skill folder**

At the root of the repository, create a new folder with your skill name:
```
skills/my-new-skill/
```

**Step 4: Add the required files**

- `skill.yaml` — The technical contract (use `_templates/skill.yaml` as a starting point)
- `README.md` — Explain what the skill does in plain English
- `examples/` — Show real examples of the skill in action (highly recommended)
- `verify.py` — A script that proves the skill works (optional but helpful)

**Step 5: Submit a pull request**

We'll review your skill and help you refine it if needed.

### Need Help?

Check the `_templates/` folder for starter files with comments explaining each field.

## Anatomy of a Skill: What's Inside

Every skill is defined by a file called `skill.yaml`. Let's break down what's in this file and why it matters.

### The Basic Information

```yaml
name: pubmed                    # A short, unique ID for the skill
display_name: PubMed Search     # The human-friendly name
version: 1.0.0                  # Version number (we update this when the skill changes)
domain: literature              # Which category it belongs to
```

### What It Does

```yaml
description: >
  Search and retrieve scientific articles from NCBI PubMed.
```

This is a plain-English explanation of the skill's purpose.

### The Contract: Inputs and Outputs

This is the most important part. It defines what information goes in and what comes out:

```yaml
interface:
  inputs:
    - name: query              # What you search for
      type: string             # It's text
      required: true           # You must provide this
  outputs:
    - name: articles           # What you get back
      type: array              # A list of articles
```

Think of this like a function signature in programming. If an agent claims to have this skill, it promises to accept these inputs and return these outputs.

### What The Agent Needs

```yaml
requirements:
  python_packages:
    - biopython>=1.80          # The agent needs this Python library
  env_vars:
    - NCBI_API_KEY             # Optional: an API key for better performance
```

This tells agent developers what tools or credentials they need to implement the skill.

## The Complete Journey: From Skill to Working Agent

Let's walk through how a skill goes from being a definition in this repository to actually working in an AI agent.

### Step 1: Discovery

A developer is building an agent for biology research. They browse this repository and find the "pubmed" skill. They think, "Perfect! My agent needs to search scientific papers."

### Step 2: Understanding

The developer reads the skill's documentation:
- The `README.md` explains what PubMed is and why it's useful
- The `skill.yaml` shows exactly what inputs the skill needs (a search query) and what it returns (a list of articles)
- The `examples/` folder shows real searches and results

### Step 3: Implementation

Now the developer writes code in their agent that:
- Accepts a search query (the input from the skill definition)
- Calls the PubMed API
- Returns a list of articles (the output from the skill definition)

Here's what that might look like in practice:

```python
from Bio import Entrez
from agno.agent import Agent
from agno.skills import Skills, LocalSkills

# Define the skill implementation
def search_pubmed(query: str, max_results: int = 10) -> dict:
    """
    Implementation of the pubmed skill.
    Follows the contract defined in skills/pubmed/skill.yaml
    """
    Entrez.email = "your.email@example.com"
    
    # Search PubMed
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()
    
    # Fetch article details
    id_list = record["IdList"]
    if not id_list:
        return {"articles": []}
    
    handle = Entrez.efetch(db="pubmed", id=id_list, rettype="medline", retmode="text")
    articles = []
    
    for pmid in id_list:
        articles.append({
            "pmid": pmid,
            "title": "Article title...",  # Parse from response
            "authors": ["Author 1", "Author 2"],
            "abstract": "Abstract text..."
        })
    
    handle.close()
    return {"articles": articles}

# Create an agent with the skill
agent = Agent(
    name="BiologyResearchAgent",
    model="gpt-4",
    skills=Skills(loaders=[LocalSkills("./skills")]),
    # Register that this agent has the pubmed skill
    capabilities=["pubmed"]
)

# The agent can now use this skill when responding to users
# When a user asks: "Find recent papers on CRISPR"
# The agent will call search_pubmed("CRISPR gene editing", max_results=5)
```

The key point: the developer can implement this however they want, as long as they follow the contract (same inputs, same output structure).

### Step 4: Registration

When the developer registers their agent with Bindu, they declare: "My agent has the 'pubmed' skill."

The platform might run verification tests to make sure the agent really can do what it claims.

### Step 5: Discovery by Users

Now when researchers browse agents, they see this agent has a "PubMed" badge. They know exactly what it can do because the skill definition is public.

### Step 6: Execution

When a user asks the agent to search for papers, the agent uses its own implementation to fulfill the request.

### The Key Insight

Skills are **contracts, not code**. The skill definition is like a promise: "If you give me X, I'll give you Y." How the agent keeps that promise is up to the developer.

## License

MIT License — see individual skill folders for specific licenses.

## Questions?

- **Documentation**: [getbindu.com/docs/skills](https://getbindu.com/docs/skills)
- **Community**: Join our Discord or post in `b/meta`
- **Issues**: Open an issue in this repository

---

Built by the Bindu community
