# Subsnatcher

Frontend for downloading and scraping subtitles from other services.</br>
Subsnacher uses [iSubRip](https://github.com/MichaelYochpaz/iSubRip).

<div align="center">
  <a href="https://github.com/miljkovicjovan/subsnatcher"><img alt="Repo Stars" src="https://img.shields.io/github/stars/miljkovicjovan/subsnatcher?style=flat&color=gold"></a>
  <a href="https://github.com/miljkovicjovan/subsnatcher/issues"><img alt="Issues" src="https://img.shields.io/github/issues/miljkovicjovan/subsnatcher?color=red"></a>
  <a href="https://github.com/miljkovicjovan/subsnatcher/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/miljkovicjovan/subsnatcher"></a>
</div>

## What is Subsnatcher?

Right now Subsnatcher allows you to scrape and dowload all subtitles from AppleTV movie website page links.

#### How to use Subsnatcher?

Right now Subsnatcher is only availabe through self hosting.
1. Clone repo
2. Install dependencies
3. Run app.py
4. Go on the link provided
5. Simply paste a movie link from an AppleTV movie page and click "Download Subtitles".
6. The page will start loading but don't worry if it takes a while, a .zip file is being created and downloaded for you.
7. Once it is finished you will get a JSON response (hopefully a success).
8. Go into the folder you of Subsnatcher and you will find a .zip file with all available subtitles for your movie.

## Current state and plans

##### Updates:

[07/11/2024] First version, simple flask self hosted server.

##### Plans:

- Website deployed so no more extra work for you :)
- Language picker.
- Download other subtitles from other services.

## Contributing

This is an open-source project for a reason, if you want to help you can.
- Innovate and create pull requests
- Test the project and create issues
- Solve current issues

## Support

Starring and sharing the project helps a lot. Thank you so much!

### Special Thanks

- [Michael Yochpaz](https://github.com/MichaelYochpaz), creator of iSubRip the idea was inspired from his project.
- All open source contributors that are also credited for their hard work bellow.

### End User License Agreement

By using SubSnatcher, you agree to the following terms:

1. Disclaimer of Affiliation:
SubSnatcher is an independent, open-source project. It is not affiliated with, endorsed by, or in any way officially connected to Apple Inc., AppleTV, or any other content provider.

2. Educational Purpose:
SubSnatcher is developed and provided solely for educational and research purposes. It demonstrates techniques for accessing and processing publicly available, unencrypted subtitle data from HLS playlists and similar sources.

3. User Responsibility and Compliance:
The use of SubSnatcher is solely at the user's own risk and discretion. Users are responsible for ensuring that their use of the tool complies with all applicable laws, regulations, and the terms of service of content providers. This includes adherence to local, state, national, and international laws.

4. Limitation of Liability:
The developers of SubSnatcher shall not be held liable for any legal consequences arising from the use of this tool. This includes, but is not limited to, claims of copyright infringement, intellectual property violations, or breaches of content providers' terms of service. Users assume all risks associated with acquiring and using subtitle data through this tool.

By using SubSnatcher, you acknowledge that you have read, understood, and agree to be bound by these terms and conditions.

### License

This project is licensed under the MIT License. For more details, see the [LICENSE file](https://github.com/miljkovicjovan/subsnatcher/blob/main/LICENSE.md).
