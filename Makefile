TARGET = steps.pdf
SRSC = steps.xml

$(TARGET) : $(SRCS)
	dblatex --param="doc.collab.show=0" --param="latex.output.revhistory=0" --backend=xetex $(SRSC)

.PHONY:
clean:
	rm $(TARGET)
