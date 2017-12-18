import vk

def main():
    token = "6f8973d86f8973d86f8973d8f36fc4348e66f896f8973d835be88fa4d56bb9569029e5a"
    ses = vk.Session(access_token=token)
    api = vk.API(ses)
    res = api.wall.get(owner_id=-103726238, count=1, filter='owner')
    # res = api.groups.getById(group_id=37213448)
    print(res[1]['text'])

if __name__ == '__main__':
    main()
