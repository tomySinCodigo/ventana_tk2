import tomllib


def getConfig(value:str) -> str:
    with open("config-vn.toml", "rb") as f:
        return tomllib.load(f)[value]

def getIcon(value:str) -> str:
    return getConfig('iconos').get(value, None)


if __name__ == '__main__':
    print(getIcon('min'))