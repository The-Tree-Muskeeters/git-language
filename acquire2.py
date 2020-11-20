"""
A module for obtaining repo readme and language data from the github API.
Before using this module, read through it, and follow the instructions marked
TODO.
After doing so, run it like this:
    python acquire.py
To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

REPOS =  ['freeCodeCamp/freeCodeCamp',
 '996icu/996.ICU',
 'vuejs/vue',
 'EbookFoundation/free-programming-books',
 'facebook/react',
 'tensorflow/tensorflow',
 'sindresorhus/awesome',
 'twbs/bootstrap',
 'jwasham/coding-interview-university',
 'kamranahmedse/developer-roadmap',
 'getify/You-Dont-Know-JS',
 'ohmyzsh/ohmyzsh',
 'CyC2018/CS-Notes',
 'donnemartin/system-design-primer',
 'github/gitignore',
 'flutter/flutter',
 'microsoft/vscode',
 'airbnb/javascript',
 'public-apis/public-apis',
 'torvalds/linux',
 'jlevy/the-art-of-command-line',
 'ytdl-org/youtube-dl',
 'axios/axios',
 'golang/go',
 'nodejs/node',
 'kubernetes/kubernetes',
 'justjavac/free-programming-books-zh_CN',
 'labuladong/fucking-algorithm',
 'microsoft/terminal',
 'denoland/deno',
 'ossu/computer-science',
 'animate-css/animate.css',
 'angular/angular',
 'tensorflow/models',
 'puppeteer/puppeteer',
 'microsoft/TypeScript',
 '30-seconds/30-seconds-of-code',
 'mrdoob/three.js',
 'ant-design/ant-design',
 'FortAwesome/Font-Awesome',
 'laravel/laravel',
 'mui-org/material-ui',
 'iluwatar/java-design-patterns',
 'PanJiaChen/vue-element-admin',
 'MisterBooo/LeetCodeAnimation',
 'angular/angular.js',
 'avelino/awesome-go',
 'moby/moby',
 'vuejs/awesome-vue',
 'nvbn/thefuck',
 'vercel/next.js',
 'webpack/webpack',
 'storybookjs/storybook',
 'goldbergyoni/nodebestpractices',
 'reduxjs/redux',
 'apple/swift',
 'jquery/jquery',
 'hakimel/reveal.js',
 'django/django',
 'atom/atom',
 'pallets/flask',
 'elastic/elasticsearch',
 'tonsky/FiraCode',
 'spring-projects/spring-boot',
 'socketio/socket.io',
 'chartjs/Chart.js',
 'shadowsocks/shadowsocks-windows',
 'expressjs/express',
 'typicode/json-server',
 'opencv/opencv',
 'keras-team/keras',
 'awesome-selfhosted/awesome-selfhosted',
 'gothinkster/realworld',
 'doocs/advanced-java',
 'chrislgarry/Apollo-11',
 'rust-lang/rust',
 'netdata/netdata',
 'adam-p/markdown-here',
 'kdn251/interviews',
 'httpie/httpie',
 'Semantic-Org/Semantic-UI',
 'xingshaocheng/architect-awesome',
 'gohugoio/hugo',
 'ElemeFE/element',
 'gatsbyjs/gatsby',
 'h5bp/html5-boilerplate',
 'josephmisiti/awesome-machine-learning',
 'lodash/lodash',
 'rails/rails',
 'h5bp/Front-end-Developer-Interview-Questions',
 'yangshun/tech-interview-handbook',
 'resume/resume.github.com',
 'bitcoin/bitcoin',
 'redis/redis',
 'ansible/ansible',
 'moment/moment',
 'nvm-sh/nvm',
 'protocolbuffers/protobuf',
 'kelseyhightower/nocode',
 'pytorch/pytorch',
 'psf/requests',
 'ReactiveX/RxJava',
 'apache/incubator-echarts',
 'papers-we-love/papers-we-love',
 'macrozheng/mall',
 'thedaviddias/Front-End-Checklist',
 'gin-gonic/gin',
 'microsoft/PowerToys',
 'mtdvio/every-programmer-should-know',
 'scikit-learn/scikit-learn',
 'ionic-team/ionic-framework',
 'meteor/meteor',
 'ReactTraining/react-router',
 'awesomedata/awesome-public-datasets',
 'jgthms/bulma',
 'jekyll/jekyll',
 'Hack-with-Github/Awesome-Hacking',
 'ryanmcdermott/clean-code-javascript',
 'necolas/normalize.css',
 'scutan90/DeepLearning-500-questions',
 'google/material-design-icons',
 'fatedier/frp',
 'ripienaar/free-for-dev',
 'Genymobile/scrcpy',
 'NARKOZ/hacker-scripts',
 'enaqx/awesome-react',
 'tuvtran/project-based-learning',
 'spring-projects/spring-framework',
 'jaywcjlove/awesome-mac',
 'neovim/neovim',
 'sveltejs/svelte',
 'google/guava',
 'aymericdamien/TensorFlow-Examples',
 'wasabeef/awesome-android-ui',
 'yarnpkg/yarn',
 'scrapy/scrapy',
 'sindresorhus/awesome-nodejs',
 'square/okhttp',
 'minimaxir/big-list-of-naughty-strings',
 'grafana/grafana',
 'prettier/prettier',
 'Dogfalo/materialize',
 'serverless/serverless',
 'azl397985856/leetcode',
 'babel/babel',
 'android/architecture-samples',
 'home-assistant/core',
 'nwjs/nw.js',
 'juliangarnier/anime',
 'tesseract-ocr/tesseract',
 'soimort/you-get',
 'ageitgey/face_recognition',
 'parcel-bundler/parcel',
 'square/retrofit',
 'MaximAbramchuck/awesome-interview-questions',
 'huggingface/transformers',
 'cdr/code-server',
 'ColorlibHQ/AdminLTE',
 'FreeCodeCampChina/freecodecamp.cn',
 'ziishaned/learn-regex',
 'astaxie/build-web-application-with-golang',
 'vsouza/awesome-ios',
 'impress/impress.js',
 'x64dbg/x64dbg',
 'gogs/gogs',
 'v2ray/v2ray-core',
 'prakhar1989/awesome-courses',
 'TryGhost/Ghost',
 'trimstray/the-book-of-secret-knowledge',
 'nodejs/node-v0.x-archive',
 'git/git',
 'bailicangdu/vue2-elm',
 '521xueweihan/HelloGitHub',
 'godotengine/godot',
 'Alamofire/Alamofire',
 'python/cpython',
 'vercel/hyper',
 'sdmg15/Best-websites-a-programmer-should-visit',
 'k88hudson/git-flight-rules',
 'florinpop17/app-ideas',
 'apache/dubbo',
 'JetBrains/kotlin',
 'prometheus/prometheus',
 'leonardomso/33-js-concepts',
 'Unitech/pm2',
 'syncthing/syncthing',
 'etcd-io/etcd',
 'justjavac/awesome-wechat-weapp',
 'deepfakes/faceswap',
 'facebook/jest',
 'junegunn/fzf',
 'AFNetworking/AFNetworking',
 'mozilla/pdf.js',
 'mermaid-js/mermaid',
 'shadowsocks/shadowsocks',
 'algorithm-visualizer/algorithm-visualizer',
 'TheAlgorithms/Java',
 'iamkun/dayjs',
 'adobe/brackets',
 'PhilJay/MPAndroidChart',
 'Solido/awesome-flutter',
 'gulpjs/gulp',
 'discourse/discourse',
 'karan/Projects',
 'nestjs/nest',
 'google/material-design-lite',
 'hexojs/hexo',
 'styled-components/styled-components',
 'slatedocs/slate',
 'traefik/traefik',
 'nuxt/nuxt.js',
 'apache/incubator-superset',
 'pixijs/pixi.js',
 'sahat/hackathon-starter',
 'alvarotrigo/fullPage.js',
 'BVLC/caffe',
 'strapi/strapi',
 'tiimgreen/github-cheat-sheet',
 'caddyserver/caddy',
 'blueimp/jQuery-File-Upload',
 'apachecn/AiLearning',
 'Marak/faker.js',
 'alex/what-happens-when',
 'dypsilon/frontend-dev-bookmarks',
 'binhnguyennus/awesome-scalability',
 'jashkenas/backbone',
 'bilibili/ijkplayer',
 'Homebrew/legacy-homebrew',
 'xitu/gold-miner',
 'preactjs/preact',
 'fastlane/fastlane',
 'huginn/huginn',
 'airbnb/lottie-android',
 'exacity/deeplearningbook-chinese',
 'tailwindlabs/tailwindcss',
 'videojs/video.js',
 'kamranahmedse/design-patterns-for-humans',
 'zenorocha/clipboard.js',
 'tldr-pages/tldr',
 'Leaflet/Leaflet',
 '0voice/interview_internal_reference',
 'isocpp/CppCoreGuidelines',
 'foundation/foundation-sites',
 'testerSunshine/12306',
 'floodsung/Deep-Learning-Papers-Reading-Roadmap',
 'php/php-src',
 'RocketChat/Rocket.Chat',
 'shadowsocks/ShadowsocksX-NG',
 'jondot/awesome-react-native',
 'photonstorm/phaser']
 

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        return repo_info.get("language", None)
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_contents = requests.get(get_readme_download_url(contents)).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data3.json", "w"), indent=1)