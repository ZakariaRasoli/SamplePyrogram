import asyncio

async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out+"\n"+ err

def tableAlign(container: list, dash: bool = True):
    lengths = [max(len(str(row[i])) for row in container) for i in range(len(container[0]))] 

    fmt = ' '.join('{:<%d}' % l for l in lengths)

    msg = fmt.format(*container[0]) + '\n'
    if dash == True:
        msg += '-' * (sum(lengths) + len(lengths) - 1) + '\n'
    for row in container[1:]:
        msg += fmt.format(*row) + '\n'
    return msg


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor