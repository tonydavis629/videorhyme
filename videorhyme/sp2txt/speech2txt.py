from speechbrain.pretrained import EncoderDecoderASR

asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-wav2vec2-commonvoice-en", savedir="pretrained_models/asr-wav2vec2-commonvoice-en")
asr_model.transcribe_file("/home/tony/github/videorhyme/videos/Biden blasts 'MAGA Republicans' as a threat to democracy/Biden blasts MAGA Republicans as a threat to democracy.webm")