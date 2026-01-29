def can_build(env, platform):
    return (env.editor_build or env["module_lightmapper_rd_enabled"])


def configure(env):
    pass
