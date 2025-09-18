def define_env(env):
    def include(filename):
        with open(f"docs/{filename}", "r", encoding="utf-8") as f:
            return f.read()
    env.macro(include)
    