import mypy.main as MAIN

import mypy.build as BUILD

py_file = "main.py"

files, opt = MAIN.process_options([py_file])

opt.preserve_asts = True
opt.fine_grained_incremental = True

result = BUILD.build(files, opt)
print(result.graph)
print(result.graph[py_file.replace(".py", "")].tree.__str__())