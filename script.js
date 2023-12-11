<!DOCTYPE html>
<html>
<head>
    <title>Website Proxy</title>
</head>
<body>
    <form onsubmit="loadWebsite(event)">
        <input type="text" id="url-input" placeholder="Enter website URL">
        <input type="submit" value="Load">
    </form>
    
    <iframe id="website-frame" style="width: 100%; height: 90vh; border: none;"></iframe>

    <script src="script.js"></script>
</body>
</html>
