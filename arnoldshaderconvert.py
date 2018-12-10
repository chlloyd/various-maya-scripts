import pymel.core as pmc
shaders = pmc.selected()

aiRoundCorner = pmc.rendering.shadingNode("aiRoundCorners", asShader = True)
aiRoundCorner.radius.set(0.05)
aiBump = pmc.rendering.shadingNode("aiBump2d", asShader = True)
aiRoundCorner.outValue >> aiBump.normal

for shader in shaders:
    aiShader = pmc.rendering.shadingNode("aiStandardSurface", asShader = True, name = "ai_jedistarfighter_{}".format(shader.getName()))
    aiShader.base.set(0)
    aiShader.baseColor.set((0,0,0))
    aiShader.subsurface.set(1)
    aiShader.subsurfaceScale.set(0.025)
    aiShader.subsurfaceType.set(1)
    aiShader.specularIOR.set(1.55)

    aiColorCorrect = pmc.rendering.shadingNode("aiColorCorrect", asShader = True)
    aiColorCorrect.saturation.set(0.75)
    aiColorCorrect.exposure.set(0.5)
    aiColorCorrect.outColor >> aiShader.subsurfaceRadius
    aiBump.outValue >> aiShader.normalCamera

    baseColor = shader.color.get()
    fileNode = None
    if shader.color.isConnected():
        fileNode = shader.color.listConnections()[0]
        fileNode.colorSpace.set("Utility - sRGB - Texture")

    aiShader.subsurfaceColor.set(baseColor)
    aiColorCorrect.input.set(baseColor)
    if fileNode:
        fileNode.outColor >> aiShader.subsurfaceColor
        fileNode.outColor >> aiColorCorrect.input

    shaderSE = shader.outColor.listConnections()[0]
    aiShader.outColor >> shaderSE.surfaceShader

    pmc.delete(shader)
