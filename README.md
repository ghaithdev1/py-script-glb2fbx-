# GLB to FBX Pipeline Converter

Automated command-line utility for batch converting `.glb` assets to game-engine ready `.fbx` format. Built specifically to optimize 3D workflows targeting Unity, Unreal Engine, and Godot.

## Technical Capabilities
* **Automated Scene Cleanup:** Purges default scene primitives, cameras, and lighting nodes during execution to deliver dependency-free assets.
* **Batch Execution:** Recursively processes all `.glb` targets within the working directory simultaneously. Non-target file formats are automatically filtered and left untouched.
* **Transform Normalization:** Corrects native scale and coordinate system discrepancies inherent to GLB-to-FBX translation, eliminating the need for manual post-scaling in runtime environments.
* **Texture Preservation:** Maintains fully mapped material and texture assignments natively.
* **Cross-Version Support:** Validated across Blender API versions spanning from **v3.0 to v5.2+**.

## Operational Guidelines
1. Deploy the script file directly into the directory containing your source `.glb` assets.
2. Execute the script within your target environment. 
3. The utility will isolate, process, and output the optimized files instantly without modifying or deleting non-GLB files.

## Technical Support & Issue Tracking
For bug tracking, deployment anomalies, or feature requests, join the dedicated technical support channel:
* **Communications Server:** https://discord.gg/f5xt5A6B5
