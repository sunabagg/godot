def can_build(env, platform):
    return (env.editor_build or env["module_xatlas_unwrap_enabled"])


def configure(env):
    pass
