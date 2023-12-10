
const GenerateAnnotations = (end) => {
    var annotations = []
    for(let i = 0; i<end; i=i+0.25) {
        annotations.push({
            from: i,
            to: i+0.5,
            type: 0
        })
    }
    return annotations
}
