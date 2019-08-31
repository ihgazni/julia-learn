
Term
----
    
    ::
        
        julia
        exit()

Install Package
===============
    
    ::
        
        using Pkg
        Pkg.add("UnicodePlots")
        ls -l ~/.julia
        

        julia> using Pkg
        julia> Pkg.add("UnicodePlots")
           Cloning default registries into `~/.julia`
           Cloning registry from "https://github.com/JuliaRegistries/General.git"
             Added registry `General` to `~/.julia/registries/General`
         Resolving package versions...
         Installed DataAPI ──────────── v1.0.1
         Installed Missings ─────────── v0.4.1
         Installed OrderedCollections ─ v1.1.0
         Installed SortingAlgorithms ── v0.3.1
         Installed DataStructures ───── v0.17.0
         Installed StatsBase ────────── v0.32.0
         Installed UnicodePlots ─────── v1.1.0
          Updating `~/.julia/environments/v1.2/Project.toml`
          [b8865327] + UnicodePlots v1.1.0
          Updating `~/.julia/environments/v1.2/Manifest.toml`
          [9a962f9c] + DataAPI v1.0.1
          [864edb3b] + DataStructures v0.17.0
          [e1d29d7a] + Missings v0.4.1
          [bac558e1] + OrderedCollections v1.1.0
          [a2af1166] + SortingAlgorithms v0.3.1
          [2913bbd2] + StatsBase v0.32.0
          [b8865327] + UnicodePlots v1.1.0
          [2a0f44e3] + Base64
          [ade2ca70] + Dates
          [8ba89e20] + Distributed
          [b77e0a4c] + InteractiveUtils
          [8f399da3] + Libdl
          [37e2e46d] + LinearAlgebra
          [56ddb016] + Logging
          [d6f4376e] + Markdown
          [de0858da] + Printf
          [9a3f8284] + Random
          [9e88b42a] + Serialization
          [6462fe0b] + Sockets
          [2f01184e] + SparseArrays
          [10745b16] + Statistics
          [8dfed614] + Test
          [4ec0a83e] + Unicode
        
        julia>

        julia> exit()
        JULIA#
        JULIA# ls -l ~/.julia/
        total 16
        drwxr-xr-x 3 root root 4096 Aug 31 01:46 environments
        drwxr-xr-x 2 root root 4096 Aug 31 01:45 logs
        drwxr-xr-x 9 root root 4096 Aug 31 01:46 packages
        drwxr-xr-x 3 root root 4096 Aug 31 01:45 registries

        
