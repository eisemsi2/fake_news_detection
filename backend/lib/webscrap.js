const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');

function TrustedUrls() {
    const trusted = new Set();
    const data = fs.readFileSync('trusted.txt', 'utf8');
    const lines = data.split(/\r?\n/);
    for (let i=0; i<lines.length; i++) {
        trusted.add(lines[i]);
    }
    return trusted;
}

function trimurl(url) {
    if (url.startsWith('/url?q=')) {
        // return url.slice(7);

        let s = "";
        for (let i=7; i<url.length; i++) {
            if (url[i] === "&") {
                break;
            }
            s += url[i];
        }
        return s;
    }
    return url;
}
function getSearchQuery(article) {
    let query = "";
    for (let i=0; i<article.length; i++) {
        query += article[i];
        if (i >= 150) {
            break;
        }
    }
    return query;

}
function getUserAgent() {
    return "Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/4.1 Chrome/62.0.3029.83 Mobile Safari/537.36"
}

async function getSomeLinks(searchQuery) {
    const trusted = TrustedUrls();
    const Query = getSearchQuery(searchQuery);
    console.log(Query);
    const searchUrl = `https://www.google.com/search?q=${encodeURIComponent(Query)}`;
    try {
        const response = await axios.get(searchUrl, {
            headers: {
                'User-Agent': getUserAgent(),
                'Accept': 'text/html'
            }
        });
        const html = response.data;
        let $ = cheerio.load(html);
        let results = [];
        $('.ezO2md').each((i,element) => {
            const url = trimurl($(element).find('a').attr('href'));
            let urlBegin = '';
            let cnt = 0;
            for (let i=0; i<url.length; i++) {
                if (url[i] === '/') {
                    cnt++;
                }
                urlBegin += url[i];
                if (cnt === 3) {
                    break;
                }
            }

            if (trusted.has(urlBegin)) {
                results.push(url);
            }
        });
        return results;
    }
    catch (error) {
        console.log(error);
        return error;
    }
}

async function getArtilce(url) {
    try {
        const response = await axios.get(url, {
            headers: {
                'User-Agent': getUserAgent(),
                'Accept': 'text/html'
            }
        });
        const html = response.data;
        let $ = cheerio.load(html);
        let article = '';
        $('p').each((i,element) => {
            article+=($(element).text());
        });
        return article;
    }
    catch (error) {
        return "error";
    }
}


module.exports = {
    getSomeLinks,
    getArtilce
};
